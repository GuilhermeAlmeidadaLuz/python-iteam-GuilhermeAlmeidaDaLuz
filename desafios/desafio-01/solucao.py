# Desafio 01 — Seu Primeiro Script
# Aluno: Guilherme Almeida da Luz
# Data:  18/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

# entrada de dados do usuário:
nome = str(input("Digite seu nome: "))
ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
hobbies = str(input("Seus hobbies: "))
ano_atual = 2026    # melhorar através de coletagem do ano atual obtido de forma dinâmica, sem atribuição direta, além de obter a data de nascimento completa

# operação para obter idade:
idade = ano_atual - ano_de_nascimento

# impressão dos dados obtidos:
print(f"Olá, {nome}.\nVocê tem {idade} ano(s) e gosta de {hobbies}")