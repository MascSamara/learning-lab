# Exibe os 15 primeiros valores da série de Fibonacci.
# Cada termo é calculado pela soma dos dois anteriores.
n1 = 0
n2 = 1

for contador in range(1, 16):
    print(n1)
    somar_dois_ultimos_numeros = n1 + n2
    n1 = n2
    n2 = somar_dois_ultimos_numeros
    



