print("------CRIANÇA ESPERANÇA------")
print("[1] Para doar R$ 10,00")
print("[2] Para doar R$ 25,00")
print("[3] Para doar R$ 50,00")
print("[4] Para doar outros valores")
print("[5] Para cancelar a doação")

opcao = int(input("Digite a opção desejada: "))
if opcao == 1:
    print(
        "Você doou R$ 10,00 para a Criança Esperança. Obrigado pela sua contribuição!"
    )
elif opcao == 2:
    print(
        "Você doou R$ 25,00 para a Criança Esperança. Obrigado pela sua contribuição!"
    )
elif opcao == 3:
    print(
        "Você doou R$ 50,00 para a Criança Esperança. Obrigado pela sua contribuição!"
    )
elif opcao == 4:
    try:
        valor = float(input("Digite o valor que deseja doar: R$ "))
        print(
            f"Você doou R$ {valor:.2f} para a Criança Esperança. Obrigado pela sua contribuição!"
        )
    except ValueError:
        print("Valor inválido. Operação cancelada.")
elif opcao == 5:
    print("Doação cancelada.")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
