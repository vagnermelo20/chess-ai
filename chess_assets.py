import os
import pygame

# Mapeamento do símbolo para o nome do arquivo
PIECE_FILENAME = {
    'K': 'wK', 'Q': 'wQ', 'R': 'wR', 'B': 'wB', 'N': 'wN', 'P': 'wP',
    'k': 'bK', 'q': 'bQ', 'r': 'bR', 'b': 'bB', 'n': 'bN', 'p': 'bP'
}

# Função para carregar uma imagem de peça
def load_piece_image(symbol, sq_size):
    name = PIECE_FILENAME[symbol]
    path = os.path.join('assets', 'pieces', f'{name}.png')
    img = pygame.image.load(path)
    img = img.convert_alpha()
    img = pygame.transform.smoothscale(img, (sq_size, sq_size))
    return img

# Função para carregar todas as imagens de peças
def load_all_piece_images(sq_size):
    images = {}
    for symbol in PIECE_FILENAME:
        images[symbol] = load_piece_image(symbol, sq_size)
    return images
