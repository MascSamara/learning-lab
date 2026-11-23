# Sistema de gerenciamento para um e-commerce
print("Olá, seja muito bem-vindo(a) ao nosso sistema!")

# Dicionário contendo o nome de cada produto e sua quantidade em estoque
produtos = {
    "Caderno": 100,
    "Lápis": 300,
    "Borracha": 200,
    "Mochila": 100,
    "Lápis de cor Castell": 3,
    "Apontador": 0,
    "Estojo": 40,
}

# Percorre cada produto e seu respectivo estoque
for mercadoria, estoque in produtos.items():

    # Se o estoque estiver zerado, interrompe completamente a verificação
    if estoque == 0:
        break

    # Se houver apenas 1 ou 2 unidades, ignora esse produto
    # e continua verificando os próximos
    if estoque == 1 or estoque == 2:
        continue

    # Se chegou até aqui, significa que o estoque é de 3 ou mais unidades
    # Portanto, o produto pode participar da promoção
    print(f"{mercadoria}: Promoção")
