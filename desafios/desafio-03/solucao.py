# Desafio 03 — Sistema de Multas
# Aluno: Guilherme Almeida da Luz
# Data:  21/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

# entrada de dados:
velocidade_atual = int( input('Digite sua velocidade em km/h: ') . strip() . split(' ') [0] )
# print(velocidade_atual)

# desvio condicional:
if velocidade_atual > 80:
    # km_excedentes = velocidade_atual - 80
    # R$ 7,00 x número de km_excedentes
    multa = 7.0 * (velocidade_atual - 80)   # multa de R$ 7,00 para cada km que passou de 80
    
    multa_formatada_em_string = str(multa)[0 : 3+1].replace('.', ',')
    print(f'Multado em R$ {multa_formatada_em_string}! Você excedeu o limite de 80km/h')

else:
    print('Boa viagem! Dirija com segurança')