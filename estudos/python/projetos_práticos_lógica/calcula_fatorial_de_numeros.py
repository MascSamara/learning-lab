# Usando a estrutura de repetição repita
# Calcula o fatorial de forma regressiva usando uma estrutura de repetição.
# Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120.
# O programa exibe tanto o processo de cálculo quanto o resultado final.

numero = int(input("Digite um número: "))
contador = numero
fatorial = 1
while contador >= 1:
    fatorial = fatorial * contador
    contador = contador - 1

print(f"O fatorial de {numero} é: {fatorial}")

# outra forma de fazer aparecendo o processo do calculo

numero = int(input("Digite um número: "))
contador = numero
fatorial = 1

while contador >= 1:
    print(contador, end="")

    fatorial = fatorial * contador
    contador = contador - 1

    if contador >= 1:
        print(" x ", end=" ")

print(f"\nO fatorial de {numero} é: {fatorial}")

# Agora usando uma estrutura de repetição dentro da outra:

numero = int(input("Digite um número: "))
contador = numero
fatorial = 1
while contador >= 1:
    fatorial = fatorial * contador
    contador = contador - 1
continuar = input("Deseja continuar?(s/n): ")
while continuar == "s":
    numero = int(input("Digite um número: "))
    contador = numero
    fatorial = 1
    while contador >= 1:
        fatorial = fatorial * contador
        contador = contador - 1
    print(f"O fatorial de {numero} é: {fatorial}")
    continuar = input("Deseja continuar?(s/n): ")


