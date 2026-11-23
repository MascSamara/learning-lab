# Script para ler 5 números do usuário, calcular a soma e encontrar o maior número.
#VARIAVEIS:
contador = 1
soma = 0
maior = None # O NONE QUER DIZER (Inicialmente, ainda não existe um maior valor definido.)

#FUNÇÃO + VARIAVES
while contador <= 5:
    numero = int(input(f"Digite o {contador}º número: "))

    soma += numero # Acumula o valor informado na soma.

# Atualiza o maior valor sempre que encontrar um número superior.
    if maior is None or numero > maior:
        maior = numero

    contador += 1 # Avança para a próxima entrada.

print(f"Soma: {soma}")
print(f"Maior número: {maior}")



