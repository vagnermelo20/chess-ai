import os
from dotenv import load_dotenv
import chess

load_dotenv()
API_KEY = os.getenv('API_KEY')

print(f'Sua API KEY é: {API_KEY}')

# Inicializa o tabuleiro de xadrez
board = chess.Board()
print(board)
