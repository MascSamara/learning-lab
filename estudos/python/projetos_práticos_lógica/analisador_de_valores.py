soma_valores = 0
media = 0
quantos_divisiveis = 0
valores_nulos = 0
soma_pares = 0

for contador in range(5):
    valor = int(input(f"Digite o {contador + 1}º número: "))

    soma_valores += valor

    if valor % 5 == 0:
        quantos_divisiveis += 1

    if valor == 0:
        valores_nulos += 1

    if valor % 2 == 0:
        soma_pares += valor

media = soma_valores / 5

print(f"Soma dos valores: {soma_valores}")
print(f"Média dos valores: {media}")
print(f"Quantidade de valores divisíveis por cinco: {quantos_divisiveis}")
print(f"Quantidade de valores nulos: {valores_nulos}")
print(f"Soma dos valores pares: {soma_pares}")
