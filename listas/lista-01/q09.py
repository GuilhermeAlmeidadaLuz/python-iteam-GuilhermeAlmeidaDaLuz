# Lista 01 — Questão 09: EAFP vs LBYL
# Aluno: Guilherme Almeida da Luz
# Data:  25/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q09.py: reescreva a função abaixo no estilo EAFP usando try/except.
# 
#   def dividir(a, b):
#       if b != 0:
#           return a / b
#       else:
#           return None
# 
# Em q09_resposta.txt: explique o que significa EAFP e qual versão é mais Pythônica.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Você tentou dividir por 0, não foi possível efetuar a operação.')
        return None

print(dividir(10, 2))
print(dividir(10, 0))