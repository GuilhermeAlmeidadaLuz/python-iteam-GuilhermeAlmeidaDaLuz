# Lista 02 — Questão 05: Funções de Alta Ordem
# Aluno: Guilherme Almeida da Luz
# Data:  29/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Em q05.py: escreva aplicar(lista, funcao) que retorna uma nova lista com a
# função aplicada a cada elemento. Demonstre com:
#   (a) função que eleva ao quadrado
#   (b) função que retorna True se o número for par
# 
# Em q05_resposta.txt: explique o que significa dizer que funções são
# 'cidadãs de primeira classe' em Python.

# ── Sua solução abaixo ──────────────────────────────────────────────────────
def aplicar(lista: list, funcao) -> list:
    nova_lista = []
    for elemento in lista:
        nova_lista.append(
            funcao(elemento)
        )
    return nova_lista

def elevar_ao_quadrado(numero: float) -> float:
    return numero ** 2

def verificar_se_numero_par(numero: int) -> bool:
    return (numero % 2 == 0)    # retorna True ou False para a comparação se o resto da divisão inteira é 0

decimais = [0.5, 1.7, 2.2, 3.6, 4.9, 5.75, 6.43]
inteiros = [0, 1, 2, 3, 4, 5, 6]

lista_resultante_1 = aplicar(lista=decimais, funcao=elevar_ao_quadrado)
print(f"{decimais} - Lista de Decimais")
print(f"{lista_resultante_1} - Lista de Decimais ao Quadrado")


lista_resultante_2 = aplicar(lista=inteiros, funcao=verificar_se_numero_par)
print(f"{inteiros} - Lista de inteiros")
print(f"{lista_resultante_2} - Números pares dentro da lista de inteiros")