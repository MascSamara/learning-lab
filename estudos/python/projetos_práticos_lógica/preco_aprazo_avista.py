produto = float(input('Digite o preço do produto: '))
descontoavista = 10/100
aprazo = 8/100
precoavista = produto - (produto * descontoavista)
precoaprazo = produto + (produto * aprazo)
print(' À vista, o preço final é: ', precoavista)
print(' À prazo, o preço final é: ', precoaprazo)
