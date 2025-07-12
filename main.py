import os
from dotenv import load_dotenv
import chess
import pygame
from chess_assets import load_all_piece_images
from chess_draw import draw_board, draw_pieces
from chess_events import handle_mouse_event
import openai

# Configurações iniciais
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')

# Inicializa o tabuleiro de xadrez
board = chess.Board()

# Configurações do pygame
pygame.init()
SIZE = 640  # Tamanho da janela
SQ_SIZE = SIZE // 8  # Tamanho de cada casa
INFO_HEIGHT = SQ_SIZE  # Altura extra para a mensagem
WIN = pygame.display.set_mode((SIZE, SIZE + INFO_HEIGHT))
pygame.display.set_caption('Chess AI')

# Cores
WHITE = (240, 217, 181)
BLACK = (181, 136, 99)

# Mapeamento das peças para Unicode
PIECE_UNICODE = {
    'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
    'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚'
}

PIECE_IMAGES = load_all_piece_images(SQ_SIZE)

# Fonte para as letras das casas
FONT = pygame.font.SysFont('arial', SQ_SIZE // 2)
selected_square = None
moving_piece = None

# Inicializa o cliente OpenAI
client = openai.OpenAI(api_key=API_KEY)

def get_status_message(board):
    if board.is_checkmate():
        return "Xeque-mate!"
    elif board.is_stalemate():
        return "Empate por afogamento!"
    elif board.is_insufficient_material():
        return "Empate por material insuficiente!"
    elif board.is_check():
        return "Xeque!"
    elif board.is_game_over():
        return "Fim de jogo!"
    else:
        return "Seu turno" if board.turn else "Turno da IA"

def ia_get_move(board):

    fen = board.fen()
    prompt = (
        "Você é um jogador de xadrez. A posição atual em FEN é: "
        f"{fen}. Qual o melhor movimento para as pretas? Responda apenas o movimento em notação UCI (exemplo: e2e4). Não use notação SAN."
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        move_str = response.choices[0].message.content.strip()
        # Verifica se é notação UCI (4 ou 5 caracteres)
        if len(move_str) in [4, 5]:
            return move_str
        # Converte SAN para UCI se necessário
        try:
            move = board.parse_san(move_str)
            return move.uci()
        except Exception:
            print(f"Resposta da IA não reconhecida: {move_str}")
            return None
    except Exception as e:
        print(f"Erro na IA: {e}")
        return None

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            selected_square, moving_piece = handle_mouse_event(event, board, selected_square, moving_piece, SQ_SIZE)
    # Limpa a tela
    WIN.fill((255, 255, 255))
    # Desenha o tabuleiro e peças
    draw_board(WIN, SQ_SIZE)
    draw_pieces(WIN, board, PIECE_IMAGES, FONT, SQ_SIZE, PIECE_UNICODE)
    # Exibe mensagem de status ABAIXO do tabuleiro
    status = get_status_message(board)
    status_text = FONT.render(status, True, (0, 0, 0))
    text_rect = status_text.get_rect(center=(SIZE // 2, SIZE + INFO_HEIGHT // 2))
    WIN.blit(status_text, text_rect)

    # Verificar com a vez da IA e o jogo não acabou
    if not board.turn and not board.is_game_over():
        move_uci = ia_get_move(board)
        if move_uci:
            try:
                move = chess.Move.from_uci(move_uci)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print(f"Movimento ilegal sugerido pela IA: {move_uci}")
            except Exception:
                print(f"Movimento inválido sugerido pela IA: {move_uci}")
        else:
            print("A IA não retornou um movimento válido.")

    pygame.display.flip()

pygame.quit()
