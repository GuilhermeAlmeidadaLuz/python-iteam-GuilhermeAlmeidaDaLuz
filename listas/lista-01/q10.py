# Lista 01 — Questão 10: Análise Crítica de Código
# Aluno: Guilherme Almeida da Luz
# Data:  25/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q10.py: reescreva a função corrigindo os 3 problemas encontrados.
# 
#   def processar_alunos(alunos=[]):
#       aprovados = []
#       for i in range(len(alunos)):
#           if alunos[i]['nota'] >= 7.0:
#               aprovados = aprovados + [alunos[i]['nome']]
#       print(aprovados)
# 
# Em q10_resposta.txt: identifique cada problema e explique por que é um problema.
# Dica: há um problema em: (1) definição da função, (2) como o loop é escrito, (3) como a lista é construída.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def processar_alunos_aprovados(alunos): # alteração do nome da função para mostrar o que ela faz de maneira específica, pois estava genérica. Além de retirar a lista vazia como valor padrão para o parâmetro da função, em caso de não ser passada, pois pode gerar erro de vazamento de dados, onde a partir da 2ª chamada da função um argumento pode se misturar com outro
    aprovados = []
    for aluno in alunos:    # o uso do range com índice e len(alunos) foi substituído, dando mais legibilidade e obtendo o mesmo resultado, pois o índice pode ser suprimido de maneira que não seja uma variável desnecessária na memória
        if aluno['nota'] >= 7.0:
            aprovados.append(aluno['nome']) # o uso de append é o padrão para adicionar elementos na lista, a maneira antiga é uma adaptação disso usando concatenação de listas, dificultando a legibilidade.
    print(aprovados)

processar_alunos_aprovados(
    [
        {
            'nome': 'Guilherme',
            'nota': 7.0,
        },
        {
            'nome': 'Gabriel',
            'nota': 6.5,
        },
        {
            'nome': 'Albert',
            'nota': 9.7,
            'curso': 'Iteam Dev FullStack'
        }
    ]
)