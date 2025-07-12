import pygame
import chess

def mouse_to_square(pos, sq_size):
    x, y = pos
    col = x // sq_size
    row = y // sq_size
    return chess.square(col, 7 - row)

def handle_mouse_event(event, board, selected_square, moving_piece, sq_size):
    if event.type == pygame.MOUSEBUTTONDOWN:
        square = mouse_to_square(event.pos, sq_size)
        piece = board.piece_at(square)
        if piece and ((piece.color == board.turn)):
            return square, piece
    elif event.type == pygame.MOUSEBUTTONUP and selected_square is not None:
        target_square = mouse_to_square(event.pos, sq_size)
        move = chess.Move(selected_square, target_square)
        if move in board.legal_moves:
            board.push(move)
        return None, None
    return selected_square, moving_piece
