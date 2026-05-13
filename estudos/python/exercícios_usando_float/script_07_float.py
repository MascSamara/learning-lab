                            #CREUZA 02
# Pergunta ao usuário quantos reais ele tem
# input() recebe o valor digitado como TEXTO
# float() converte esse texto para número decimal
reais = float(input('Quantos reais eu tenho? '))

# Converte o valor de reais para dólares
# Aqui estamos assumindo que 1 dólar = 5.22 reais
dolar = reais / 5.22

# Mostra o resultado na tela
# f"" permite colocar variáveis dentro do texto
# {dolar:.2f} significa mostrar o valor com 2 casas decimais
print(f"Posso ter {dolar:.2f} dólares")

