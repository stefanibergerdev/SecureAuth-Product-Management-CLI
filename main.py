import seguranca, math

def calcular_preco_com_desconto(preco, desconto=10):
    preco_com_desconto = preco - (preco * (desconto / 100))
    return preco_com_desconto

def formatar_moeda(valor):
    return f"R$ {valor:.2f}"

nome_usuario = input("Digite seu nome de usuário: ")
token_gerado = seguranca.gerar_token(nome_usuario)

seguranca.registrar_log(nome_usuario, "LOGIN_SUCESSO")
print(f"Token gerado para {nome_usuario}: {token_gerado}")

estoque = []

while True:
    try:
        qtd_produtos = int(input("Quantidade de produtos para cadastrar: "))
        if qtd_produtos > 0:
            break  
        print("Digite um número maior que zero.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


for i in range(qtd_produtos):
    print(f"\n--- Cadastro do Produto {i + 1} ---")
    
    
    while True:
        try:
            preco = float(input(f"Digite o preço do produto {i + 1}: "))
            if preco > 0:
                break  
            print("Preço inválido. Digite um valor maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número decimal válido.")

    
    preco_com_desconto = calcular_preco_com_desconto(preco)
    preco_formatado = formatar_moeda(preco_com_desconto)
    
    
    item = {
        "produto": i + 1,
        "preco_original": preco,
        "preco_com_desconto": preco_formatado
    }
    
    estoque.append(item)
        
print("\n--- Estoque Cadastrado ---")
for item in estoque:
    print(f"Produto {item['produto']}: {item['preco_com_desconto']}")