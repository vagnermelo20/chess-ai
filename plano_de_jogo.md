# Plano de Integração da IA no Chess-AI

## Objetivo
Integrar uma IA ao jogo de xadrez, garantindo que o contexto enviado para a IA seja sempre a posição atual do tabuleiro, e que a IA jogue automaticamente quando for seu turno.

---

## Etapas do Plano

1. **Definir Momento de Ação da IA**
   - A IA deve jogar automaticamente quando for o turno dela (por exemplo, quando `board.turn == False`).

2. **Gerar Contexto da Partida**
   - Sempre que for a vez da IA, envie a posição atual do tabuleiro para a API.
   - Utilize a notação FEN (`board.fen()`) ou PGN para representar o estado do jogo.

3. **Enviar Requisição para a API**
   - Monte uma mensagem clara para a IA, incluindo o contexto (posição atual) e solicite o melhor movimento.

4. **Receber e Interpretar Resposta**
   - Parseie a resposta da IA para obter o movimento sugerido (em notação SAN ou UCI).
   - Valide se o movimento é legal antes de executá-lo.

5. **Executar Movimento da IA**
   - Aplique o movimento sugerido no tabuleiro usando `board.push()`.

6. **Atualizar Interface e Status**
   - Após o movimento da IA, atualize o tabuleiro e as mensagens de status.
   - Continue alternando turnos normalmente.

7. **Tratar Erros e Situações Especiais**
   - Lide com respostas inválidas, movimentos ilegais ou falhas na API.
   - Garanta que o jogo não trave e que o usuário seja informado.

---

## Fluxo Resumido
Usuário faz um movimento → verifica se é a vez da IA → envia contexto atual para a IA → recebe e executa o movimento da IA → atualiza interface → repete.

---

## Observações
- O contexto da IA deve sempre refletir a posição atual do tabuleiro.
- O sistema deve ser robusto para lidar com erros e garantir boa experiência ao usuário.
- O plano pode ser refinado conforme avanços no desenvolvimento.
