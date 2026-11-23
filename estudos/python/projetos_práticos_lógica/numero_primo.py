numero = int(input("Digite um número: "))
contador = 1
contDiv = 0
while contador < numero:
    contador = contador + 1
    if numero % contador == 0:
        print(f"{numero} é divisível por {contador}")
        contDiv = contDiv + 1
if contDiv == 0:
    print(f"{numero} é um número primo!")
else:
    print(f"{numero} não é um número primo.")
print("Ao todo existe",contDiv, "divisore(s)")