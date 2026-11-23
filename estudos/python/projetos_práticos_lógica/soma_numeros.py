# Usando a estrutura de repetição PARA


numero = 0
contador = 1
soma = 0

for contador in range(1, 6):
    numero = float(input(f"Digite o {contador}º número: "))
    soma += numero

print(f"A soma dos números é: {soma}")