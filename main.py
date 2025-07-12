import os
from dotenv import load_dotenv
import chess
import pygame

# Configurações iniciais
load_dotenv()
API_KEY = os.getenv('API_KEY')
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

# Carregar imagens das peças
PIECE_IMAGES = {}
PIECE_IMAGES['b'] = pygame.image.load(os.path.join('assets', 'pieces', 'bB.png'))
PIECE_IMAGES['b'] = pygame.transform.smoothscale(PIECE_IMAGES['b'], (SQ_SIZE, SQ_SIZE))
PIECE_IMAGES['k'] = pygame.image.load(os.path.join('assets', 'pieces', 'bK.png'))
PIECE_IMAGES['k'] = pygame.transform.smoothscale(PIECE_IMAGES['k'], (SQ_SIZE, SQ_SIZE))
PIECE_IMAGES['n'] = pygame.image.load(os.path.join('assets', 'pieces', 'bN.png'))
PIECE_IMAGES['n'] = pygame.transform.smoothscale(PIECE_IMAGES['n'], (SQ_SIZE, SQ_SIZE))
PIECE_IMAGES['q'] = pygame.image.load(os.path.join('assets', 'pieces', 'bQ.png'))
PIECE_IMAGES['q'] = pygame.transform.smoothscale(PIECE_IMAGES['q'], (SQ_SIZE, SQ_SIZE))
PIECE_IMAGES['r'] = pygame.image.load(os.path.join('assets', 'pieces', 'bR.png'))
PIECE_IMAGES['r'] = pygame.transform.smoothscale(PIECE_IMAGES['r'], (SQ_SIZE, SQ_SIZE))
PIECE_IMAGES['p'] = pygame.image.load(os.path.join('assets', 'pieces', 'bP.png'))
PIECE_IMAGES['p'] = pygame.transform.smoothscale(PIECE_IMAGES['p'], (SQ_SIZE, SQ_SIZE))

# Função para desenhar o tabuleiro
def draw_board(win):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(win, color, (col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))

# Função para desenhar as peças
FONT = pygame.font.SysFont('arial', SQ_SIZE // 2)
def draw_pieces(win, board):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)
            symbol = piece.symbol()
            if symbol in PIECE_IMAGES:
                win.blit(PIECE_IMAGES[symbol], (col*SQ_SIZE, row*SQ_SIZE))
            else:
                text = FONT.render(PIECE_UNICODE[symbol], True, (0, 0, 0))
                text_rect = text.get_rect(center=(col*SQ_SIZE + SQ_SIZE//2, row*SQ_SIZE + SQ_SIZE//2))
                win.blit(text, text_rect)

selected_square = None
moving_piece = None

# Função para converter coordenadas de mouse para casa do tabuleiro
def mouse_to_square(pos):
    x, y = pos
    col = x // SQ_SIZE
    row = y // SQ_SIZE
    # O tabuleiro do python-chess começa do canto inferior esquerdo
    return chess.square(col, 7 - row)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            square = mouse_to_square(event.pos)
            piece = board.piece_at(square)
            if piece and ((piece.color == board.turn)):  # Só pode mover peça do turno
                selected_square = square
                moving_piece = piece
        elif event.type == pygame.MOUSEBUTTONUP and selected_square is not None:
            target_square = mouse_to_square(event.pos)
            move = chess.Move(selected_square, target_square)
            if move in board.legal_moves:
                board.push(move)
            selected_square = None
            moving_piece = None
    draw_board(WIN)
    draw_pieces(WIN, board)
    pygame.display.flip()

pygame.quit()
