# Contagem Inteligente que indentidica o número digitado se for do maior para o menor o sistema intentifica e faz a contagem progresiva dos numeros digitados pelo usuário ex: de 0 a 10. Caso contrário se o numero for do menor para o maior o sistema faz a contagem regressiva dos numeros digitados pelo usuário ex: de 10 a 0.

print("Digite dois números para que o sistema faça a contagem entre eles:")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

    # i = variável que recebe cada número da contagem
    # in = indica que i vai receber valores de uma sequência
    # range = cria a sequência de números que será percorrida
    # > = verifica se o numero1 é maior que o numero2
if numero1 > numero2:
    print("-------Contando-------")
    for i in range(numero1, numero2 - 1, -1):
        print(i)

else:
    print("-------Contando-------")
    for i in range(numero1, numero2 + 1):
        print(i)


