# Desafio 02 — Calculadora de IMC
# Aluno: Guilherme Almeida da Luz
# Data: 21/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

# entradas do usuário:
nome_do_usuario = input('Digite seu nome: ')
peso_do_usuario = float(input('Digite seu peso em \'Kg\' (exemplo: 81.2): '))
altura_do_usuario = float(input('Digite sua altura em \'M\' (exemplo: 1.75): '))

# print(type(peso_do_usuario))
# print(type(altura_do_usuario))

# processamento: cálculo do IMC = peso / altura**2
valor_imc = peso_do_usuario / altura_do_usuario**2

# saída exibida na tela:
print(f'Olá {nome_do_usuario}, seu IMC é {valor_imc:.2f}')