produto = float(input('Qual o valor do produto? '))
preco = produto * 60/100
imposto = produto - preco
print(f"O valor do imposto é: {imposto:.2f}")