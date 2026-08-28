# Pergunta qual foi o valor do empréstimo
# input() recebe o valor como texto
# float() transforma em número decimal para fazer cálculos
valor = float(input("Qual o valor do empréstimo? "))

# Pergunta em quantas parcelas ela quer pagar
# int() transforma o valor digitado em número inteiro
parcelas = int(input("Em quantas parcelas deseja pagar? "))

# Calcula 20% de juros sobre o valor
# 20/100 significa 20%
juros = valor * 20/100

# Soma o valor do empréstimo com os juros
# Esse será o valor total da dívida
total = valor + juros

# Calcula o valor de cada parcela
# Divide o valor total pela quantidade de parcelas
parcela = total / parcelas

# Mostra os resultados
# f-string permite colocar variáveis dentro do texto
# :.2f mostra apenas 2 casas decimais
print(f"Valor total com juros: {total:.2f}")
print(f"Valor de cada parcela: {parcela:.2f}")
