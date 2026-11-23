print("----- SUPER CONTADOR -----")

# Apresenta as opções e recebe a escolha do usuário
opcoes = int(
    input(
        "Digite:\n[1] Para contar de 1 até 10\n[2] Para contar de 10 até 1\n[3] Para sair\nEscolha uma opção: "
    )
)

# Opção 1: contagem crescente
if opcoes == 1:
    numero = 1
    while numero <= 10:
        print(numero)
        numero += 1

# Opção 2: contagem regressiva
elif opcoes == 2:
    numero = 10
    while numero >= 1:
        print(numero)
        numero -= 1

# Opção 3: sair
elif opcoes == 3:
    print("Saindo do programa...")

# Caso o usuário digite uma opção inexistente
else:
    print("Opção inválida!")
