# Pergunta ao usuário qual é o valor do produto
# input() recebe o valor digitado como TEXTO
# float() converte esse texto para número decimal para podermos fazer cálculos
produto = float(input('Qual o valor do produto? '))

# Calcula 60% do valor do produto
# 60/100 significa 60 por cento
# Multiplicamos o valor do produto por 0.60
preco = produto * 60/100

# Calcula o valor do imposto
# Aqui o programa pega o valor total do produto
# e subtrai os 60% calculados anteriormente
imposto = produto - preco

# Mostra o valor do imposto na tela
# f"" permite colocar variáveis dentro do texto
# {imposto:.2f} faz o número aparecer com 2 casas decimais
print(f"O valor do imposto é: {imposto:.2f}")
