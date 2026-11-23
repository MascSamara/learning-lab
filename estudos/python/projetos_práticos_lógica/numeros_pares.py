# Mostra os numeros pares de 0 até o valor digitedo pelo usuário
contador=0
valor = float(input("Digite um valor: "))
for contador in range(0, int(valor)):
    if contador % 2 == 0:
        print(contador)

# Agora Contagem regressiva de números pares

contador=0
valor = float(input("Digite um valor: "))
if valor % 2 != 0:
    valor -= 1

for contador in range(int(valor), -1, -2):
    print(contador)