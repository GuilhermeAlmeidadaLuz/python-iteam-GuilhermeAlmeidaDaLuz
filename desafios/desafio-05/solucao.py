# Desafio 05 — Gerenciador de Compras
# Aluno: Guilherme Almeida da Luz
# Data:  24/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

lista_de_produtos = []
while True:
    entrada = str(input('Digite o nome de um produto ou \'fim\' para sair: ').strip().title())
    if entrada.lower() == 'fim':
        break
    else:
        lista_de_produtos.append(entrada)

print( ('=' * 100) + '\n' + 'Lista de Produtos:'.center(100, ' ')  + '\n' + ('=' * 100) )
ajuste_numeracao = len(f'{len(lista_de_produtos)}') # pega a quantidade de produtos, coloca dentro de uma string e recalcula o tamanho para saber a quantidade de dígitos utilizados.
for indice, produto in enumerate(lista_de_produtos):
    print(f'item {indice + 1 :>{ajuste_numeracao}} - {produto}')
print(('=' * 100) + '\n' + f'Total de ítens: {len(lista_de_produtos)}')