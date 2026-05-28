# Lista 02 — Questão 03: Sistema de Inventário
# Aluno: Guilherme Almeida da Luz
# Data:  27/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Implemente com lista de dicionários:
#   1. adicionar_produto(inventario, nome, codigo, quantidade, preco)
#   2. buscar_por_codigo(inventario, codigo)  → produto ou None
#   3. listar_abaixo_do_minimo(inventario, minimo)
#   4. valor_total(inventario)  → soma de quantidade × preço
# Use funções para cada operação. Demonstre as 4 no código principal.

# ── Sua solução abaixo ──────────────────────────────────────────────────────

inventario_de_produtos = []

def adicionar_produto(inventario, nome, codigo, quantidade, preco):
    inventario.append(
            {
                "nome": nome,
                "codigo": codigo,
                "quantidade": quantidade,
                "preco": preco
            }
        )
    print("\n\tProduto adicionado...\n")

def buscar_por_codigo(inventario, codigo) -> dict | None:
    for produto in inventario:
        if produto.get("codigo") == codigo:
            return (
                f"Código: {produto.get("codigo")} \t-\t " +
                f"Nome: {produto.get("nome")} \t-\t " +
                f"Quantidade: {produto.get("quantidade")} \t-\t " +
                f"Preço: {produto.get("preco"):.2f}"
            )    
    return None

def listar_abaixo_do_minimo(inventario, minimo):
    print("\n\tProdutos:\n")
    contagem = 0
    for produto in inventario:
        if produto.get("preco") < minimo:
            print(
                f"Código: {produto.get("codigo")} \t-\t "
                f"Nome: {produto.get("nome")} \t-\t "
                f"Quantidade: {produto.get("quantidade")} \t-\t "
                f"Preço: {produto.get("preco"):.2f}"
            )
            contagem += 1
    if contagem == 0:
        print(f"\nNenhum produto abaixo de R${minimo:.2f}...")

def valor_total(inventario) -> float:
    soma_total = 0
    for produto in inventario:
        soma_total += produto.get("quantidade") * produto.get("preco")
    return soma_total
    
menu = """
======================================
        Inventário de Produtos
======================================
a - adicionar produto
b - buscar por código
l - listar produtos abaixo do valor mínimo
v - valor total
s - sair
======================================
"""

while True:
    print(menu)
    opcao = str(input("Digite uma opção: "))
    codigo_do_produto = None
    match opcao.lower():
        case 'a':
            print("=" * 51 +
                  "\n" + 
                  "Adicionar Produto".center(49) + 
                  "\n" + 
                  "=" * 51)
            
            nome_do_produto = str(input("Nome do Produto: ").strip())
            if len(nome_do_produto) >= 2:
                try:
                    codigo_do_produto = int(input("Código do Produto: ").strip())
                    quantidade_do_produto = int(input("Quantidade: ").strip())
                    preco_do_produto = float(input("Preço: R$ ").strip())
                except ValueError:
                    print("\n\tErro: Não foi possível usar o valor digitado, deve ser um número!\n")
                else:
                    adicionar_produto(inventario = inventario_de_produtos, nome = nome_do_produto, codigo = codigo_do_produto, quantidade = quantidade_do_produto, preco = preco_do_produto)
            else:
                print("\n\tErro: Nome do produto não digitado ou inválido. Tente novamente...\n")
        case 'b':
            print("="*51 + "\n" + "Buscar Produto por Código".center(49) + "\n" + "="*51)
            codigo_do_produto = int(input("Código do produto: "))
            
            encontrado = buscar_por_codigo(inventario = inventario_de_produtos, codigo = codigo_do_produto)
            if not encontrado:
                print("\n[Resultado da Busca]\nProduto não encontrado...")
            else:
                print(f"\n[Resultado da Busca]\n{encontrado}")
        case 'l':
            print(f"{"="*51}"
                  "\n"
                  f"{"Listar Produtos Abaixo do Mínimo".center(49)}"
                  "\n"
                  f"{"="*51}")
            valor_minimo = float(input("Digite o valor mínimo: "))
            listar_abaixo_do_minimo(inventario=inventario_de_produtos, minimo=valor_minimo)
        case 'v':
            print(f"{"="*51}"
                  "\n"
                  f"{"Valor Total em Produtos".center(49)}"
                  "\n"
                  f"{"="*51}")
            print(f"\nR$ {valor_total(inventario=inventario_de_produtos):.2f}\n")
        case 's':
            print("\nEncerrando o sistema...\n")
            break
        case _:
            print("\nOpção inválida, tente novamente...\n")