Esse projeto vai ser para permitir jogar uma partida de xadrez contra a IA. Eu irei pegar a api key que ta no meu .env

Após isso, eu criarei um assistente que será o jogador de xadrez que eu vou contra e o contexxto que será passado é ssempre a situação atual da partida. eu quero que esse jogo seja com interface gráfica estilo sites de xadrez, permitindo mover as peças com o mouse.

---

## Plano do Projeto Chess AI

### Objetivo
Criar um jogo de xadrez jogável com interface gráfica 8x8, onde o usuário enfrenta uma IA usando uma API key do .env. O usuário poderá mover as peças arrastando com o mouse, igual aos sites de xadrez.

### Etapas do Projeto
1. Configurar ambiente (.env, requirements.txt)
2. Utilizar biblioteca gráfica (pygame ou tkinter)
3. Desenhar tabuleiro 8x8 e peças
4. Implementar movimentação por mouse (arrastar e soltar)
5. Integrar lógica do xadrez (python-chess)
6. Integrar com API de IA para movimentos do adversário
7. Validar movimentos e alternar turnos
8. Detectar xeque, xeque-mate e empate
9. Exibir mensagens de status
10. Refinar interface e experiência
11. Documentar o projeto

### Tecnologias sugeridas
- python-chess
- python-dotenv
- openai ou similar
- pygame ou tkinter

### Próximos passos
- Criar arquivo .env com API key
- Adicionar dependências no requirements.txt
- Implementar estrutura inicial no main.py
- Configurar ambiente de desenvolvimento

### Observação
O projeto será visual, permitindo jogabilidade intuitiva e interativa, como nos principais sites de xadrez.