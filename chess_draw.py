import pygame
import chess

WHITE = (240, 217, 181)
BLACK = (181, 136, 99)

# Função para desenhar o tabuleiro
def draw_board(win, sq_size):
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(win, color, (col*sq_size, row*sq_size, sq_size, sq_size))

# Função para desenhar as peças
def draw_pieces(win, board, piece_images, font, sq_size, piece_unicode):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)
            symbol = piece.symbol()
            if symbol in piece_images:
                win.blit(piece_images[symbol], (col*sq_size, row*sq_size))
            else:
                text = font.render(piece_unicode[symbol], True, (0, 0, 0))
                text_rect = text.get_rect(center=(col*sq_size + sq_size//2, row*sq_size + sq_size//2))
                win.blit(text, text_rect)
