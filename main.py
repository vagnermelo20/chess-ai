import os
from dotenv import load_dotenv
import chess
import pygame
from chess_assets import load_all_piece_images
from chess_draw import draw_board, draw_pieces
from chess_events import handle_mouse_event

# Configurações iniciais
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')
print(f'Sua API KEY é: {API_KEY}')

# Inicializa o tabuleiro de xadrez
board = chess.Board()

# Configurações do pygame
pygame.init()
SIZE = 640  # Tamanho da janela
SQ_SIZE = SIZE // 8  # Tamanho de cada casa
WIN = pygame.display.set_mode((SIZE, SIZE))
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

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            selected_square, moving_piece = handle_mouse_event(event, board, selected_square, moving_piece, SQ_SIZE)
    draw_board(WIN, SQ_SIZE)
    draw_pieces(WIN, board, PIECE_IMAGES, FONT, SQ_SIZE, PIECE_UNICODE)
    # Exibe mensagem de status
    status = get_status_message(board)
    status_text = FONT.render(status, True, (0, 0, 0))
    WIN.blit(status_text, (10, 10))
    pygame.display.flip()

pygame.quit()
