#Conversor de moedas: real para dólar e euro
real = float(input('Digite o valor em reais que você deseja converter:'))
dolar = real / 5.15
euro = real / 5.95

print(f'Com {real:.2f} reais você pode comprar $ {dolar:.2f} dólares e {euro:.2f} euros.')
