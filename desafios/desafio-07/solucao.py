# Desafio 07 — Bio-Calculadora
# Aluno: Guilherme Almeida da Luz
# Data:  26/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────
import funcoes_mat

print("""
1 - Área do Círculo
2 - Volume da Esfera
3 - Hipotenusa do Triângulo
""")
calculo_desejado = int(input("Digite o número desejado: "))

match calculo_desejado:
    case 1:
        print(' Cálculo de Área do Círculo: '.center(100, "#"))
        raio_digitado = float(input("Digite o raio do círculo: "))

        resultado = funcoes_mat.area_do_circulo(raio = raio_digitado)
        print(f"Área do Círculo: {resultado:.2f} u.m.²")
    case 2:
        print(' Volume da Esfera: '.center(100, "#"))
        raio_digitado = float(input("Digite o raio da esfera: "))

        resultado = funcoes_mat.volume_da_esfera(raio = raio_digitado)
        print(f"Volume da Esfera: {resultado:.2f} u.m.³")
    case 3:
        print(' Hipotenusa do Triângulo Retângulo: '.center(100, "#"))
        cateto_a = int(input("Digite um número inteiro para o cateto A: "))
        cateto_b = int(input("Digite um número inteiro para o cateto B: "))

        resultado = funcoes_mat.hipotenusa(cateto_a=cateto_a, cateto_b=cateto_b)
        print(f"Hipotenusa de um Triângulo Retângulo: {resultado:.0f} u.m.")
    case _:
        print('Você não digitou um opção válida!')