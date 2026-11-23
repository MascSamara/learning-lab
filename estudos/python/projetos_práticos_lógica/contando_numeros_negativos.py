# Cotagem numeros negativos, o usuário digita os números e o programa conta quantos são negativos, no final mostra os números digitados e quais deles são negativos. Sendo que os negativos sãos os números menores que 0,ou seja no programa o número 0 não é considerado negativo e eles devem aparecer com o simbolo de menos na frente do número.
numeros = 0
quantidade_numeros = int(input("Quantos números você quer digitar?"))
numeros_negativos = 0
numeros_digitados = []
numeros_negativos_lista = []
while len(numeros_digitados) < quantidade_numeros:

    numero = int(input("Digite um número:"))
    numeros_digitados.append(numero)
    if numero < 0:
        numeros_negativos_lista.append(numero)
        numeros_negativos += 1

print(
    f"foi digitado {numeros_negativos} número(s) negativo(s), que são: {numeros_negativos_lista}"
)
