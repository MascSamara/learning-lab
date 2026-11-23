#Exibe a tabuada de um número qualquer

contador = 1
numero = int(input("Digite um número para ver a tabuada: "))
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
