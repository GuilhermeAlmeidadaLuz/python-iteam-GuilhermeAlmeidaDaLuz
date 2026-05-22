# Lista 01 — Questão 06: Validador de Senha
# Aluno: Guilherme Almeida da Luz
# Data:  22/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Escreva um programa que solicite uma senha em loop até que atenda TODOS:
#   1. Mínimo 8 caracteres.
#   2. Pelo menos um dígito (use .isdigit() em cada caractere).
#   3. Pelo menos uma letra maiúscula.
# Para cada tentativa inválida, informe qual critério não foi atendido.
# Ao aceitar: 'Senha válida após X tentativa(s).'

# ── Sua solução abaixo ──────────────────────────────────────────────────────


# ------------------------- VERSÃO 1 -----------------------

senha_valida = False
tentativas = 0
while (not senha_valida):
    senha = str(input('Digite a senha: '))
    
    #   1. Mínimo 8 caracteres.
    tem_mais_de_oito_caracteres = True if len(senha) >= 8 else False
   
    #   2. Pelo menos um dígito (use .isdigit() em cada caractere).
    verifica_digitos = [True for caracter in senha if caracter.isdigit()]
    tem_um_digito = True in verifica_digitos
    # print(verifica_digitos)
   
    #   3. Pelo menos uma letra maiúscula.
    verifica_letras_maisculas = [True for caracter in senha if caracter.isupper()]
    tem_uma_letra_maiuscula = True in verifica_letras_maisculas
    # print(verifica_letras_maisculas)
    
    # verifica se os 3 casos foram atendidos
    if tem_mais_de_oito_caracteres and tem_um_digito and tem_uma_letra_maiuscula:
        senha_valida = True
    else:
        tentativas += 1

# exibe no terminal depois que o loop encerrar:
print(f"Senha válida após {tentativas} tentativa(s).")  

# ------------------------- VERSÃO 2 -----------------------

senha_valida = False
tentativas = 0

while (not senha_valida):
    senha = str(input("Digite a senha: "))

    # 1. Mínimo 8 caracteres.
    minimo_8_caracteres = False
    if len(senha) >= 8:
        minimo_8_caracteres = True

    # 2. Pelo menos um dígito (use .isdigit() em cada caractere).
    pelo_menos_um_digito = False
    for caractere in senha:
        if caractere.isdigit():
            pelo_menos_um_digito = True
            break

    # 3. Pelo menos uma letra maiúscula.
    pelo_menos_uma_maiuscula = False
    for caractere in senha:
        if caractere.isupper():
            pelo_menos_uma_maiuscula = True
            break
    
    # verificação final - verifica se os 3 casos foram atendidos:
    if minimo_8_caracteres and pelo_menos_um_digito and pelo_menos_uma_maiuscula:
        senha_valida = True
    else:
        tentativas = tentativas + 1

# exibe no terminal depois que o loop encerrar:
print(f"Senha válida após {tentativas} tentativa(s).")

# ------------------------ VERSÃO 3 ------------------------
senha_valida = False
tentativas = 0

while (not senha_valida):
    senha = str(input("Digite a senha: "))

    # 1. Mínimo 8 caracteres.
    
    minimo_8_caracteres = False
    if len(senha) >= 8:
        minimo_8_caracteres = True

    # 2. Pelo menos um dígito (use .isdigit() em cada caractere).
    # 3. Pelo menos uma letra maiúscula.

    pelo_menos_um_digito = False
    pelo_menos_uma_maiuscula = False
    for caractere in senha:
        if caractere.isdigit():
            pelo_menos_um_digito = True
            # break
        
        if caractere.isupper():
            pelo_menos_uma_maiuscula = True
            
        if pelo_menos_um_digito and pelo_menos_uma_maiuscula:
            break

    # # verificação final - verifica se os 3 casos foram atendidos:
    if minimo_8_caracteres and pelo_menos_um_digito and pelo_menos_uma_maiuscula:
        senha_valida = True
    else:
        # acrescenta o número de tentativas
        tentativas = tentativas + 1

# exibe no terminal depois que o loop encerrar:
print(f"Senha válida após {tentativas} tentativa(s).")    