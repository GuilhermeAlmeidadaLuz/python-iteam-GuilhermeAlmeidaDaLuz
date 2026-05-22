# Desafio 04 — Tabuada Personalizada
# Aluno: Guilherme Almeida da Luz
# Data:  21/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

# entrada de dados do usuário:
while True:
    numero_escolhido = int(input('Digite um número de 1 a 10. Para sair, digite \'0\': '))
    if numero_escolhido == 0:
        break
    elif (numero_escolhido > 10) or (numero_escolhido < 0):
        continue
    else:
        for i in range(1, 10 + 1, 1):
            print(f'{numero_escolhido:2} x {i:2} = {(numero_escolhido * i):3}')
    