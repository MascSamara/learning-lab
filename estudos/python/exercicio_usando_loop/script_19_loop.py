#CONVERSOR DE MOEDAS:
# Pergunta ao usuário quantos reais ele tem
# input() recebe o valor digitado como TEXTO
# float() converte esse texto para número decimal
reais = float(input('Quantos reais eu tenho? '))

# Converte o valor de reais para dólares
# Aqui estamos assumindo que 1 dólar = 5.22 reais
dolar = reais / 5.096
contador = 1
if contador <= 4:
# Mostra o resultado na tela
# f"" permite colocar variáveis dentro do texto
# {dolar:.2f} significa mostrar o valor com 2 casas decimais
    print(f"O valor convertido é US$  {dolar:.2f} ")
contador= contador +1
while contador <= 4:
    reais = float(input('Quantos reais eu tenho? '))
    dolar = reais / 5.096
    print(f"O valor convertido é US$  {dolar:.2f} ")
    contador= contador +1