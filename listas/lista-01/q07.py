# Lista 01 — Questão 07: Progressão e Análise
# Aluno: Guilherme Almeida da Luz
# Data:  23/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas).
# Exiba: maior nota, menor nota, média, quantidade acima da média e
# classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
# Explique em comentários por que escolheu for ou while em cada parte.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

# 1. Leia 10 notas (0.0–10.0) com validação (try/except + while para inválidas). 
contador = 1
notas = []
while (contador <= 10): # enquanto não atingir a contagem de notas, vai repetir, mas com um porém: se a nota não for válida, não incrementa o contador para repetir a nota
    try:
        nota = float(input(f'Digite a nota {contador:>2}: '))
        if (nota >= 0) and (nota <= 10):
            notas.append(nota)
            contador += 1
        else:
            print(f'ERRO: Nota {nota} fora do intervalo permitido [0.0 - 10.0]! Tente novamente...')
    except ValueError:  # se digitar algo diferente de um número, captura erro e exibe mensagem para correção
        print('\nERRO: Você digitou uma nota inválida! Tente novamente...\n')

# 2. Exiba: maior nota, menor nota, média, quantidade acima da média e classificação (Aprovado ≥ 7.0, Recuperação ≥ 5.0, Reprovado).
print('\n\tRelatório de Notas:\t\n'.center(100, '='))

maior_nota = notas[0]
menor_nota = notas[0]
media = sum(notas) / len(notas)
quantidade_de_notas_acima_da_media = 0
for nota in notas:
    if nota >= maior_nota:
        maior_nota = nota
    
    if nota <= menor_nota:
            menor_nota = nota
    
    if nota > media:
        quantidade_de_notas_acima_da_media += 1

print(f'Maior nota: {maior_nota}' + '\n' + f'Menor nota: {menor_nota}' + '\n' + f'Média: {media}' + '\n' + f'Quantidade de Notas acima da média: {quantidade_de_notas_acima_da_media}')

for indice, nota in enumerate(notas):
    if (nota >= 7.0):
        print(f'Nota {indice + 1 :>2} - {nota:>4} - Aprovado')
    elif (nota >= 5.0):
        print(f'Nota {indice + 1 :>2} - {nota:>4} - Recuperação')
    else:
        print(f'Nota {indice + 1 :>2} - {nota:>4} - Reprovado')
