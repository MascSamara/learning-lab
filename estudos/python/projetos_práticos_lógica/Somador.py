# Estrutura de repetição usando o comando repita

soma = 0
contador = 1
while contador <= 5:
    numero = float(input(f"Digite o {contador}º número: "))
    soma += numero
    contador += 1

print(f"A soma dos números é: {soma}")

# usaando o while porém o usuário poderá escolher quantos números deseja somar
n = int(input("Quantos números você deseja somar? "))
soma = 0
contador = 1
while contador <= n:
    numero = float(input(f"Digite o {contador}º número: "))
    soma += numero
    contador += 1

print(f"A soma dos números é: {soma}")
