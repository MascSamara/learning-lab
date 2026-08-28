# Loop de 1 a 1000 e diz qual é o numero par ou impar
# cria um loop (laço de repetição)
# a variável "numero" vai receber cada valor dentro do intervalo
# range(1,10001) gera números de 1 até 10000
# (o último número do range não entra, por isso usamos 10001)
for numero in range(1,10001):

    # % é o operador módulo (resto da divisão)
    # aqui verificamos se o número dividido por 2 tem resto 0
    # se tiver resto 0, o número é par
    if numero %2 == 0:

        # f-string permite colocar a variável dentro do texto
        # aqui mostramos que o número é par
        print(f'{numero} é par')

    else:

        # se o resto da divisão por 2 não for 0
        # significa que o número é ímpar
        print(f'{numero} é ímpar')
