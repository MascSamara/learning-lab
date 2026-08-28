# pede ao usuário para escolher qual operação deseja fazer
# o input recebe o valor digitado e int() converte para número inteiro
opcao = int(input('Escolha uma opção: '))

# pede o primeiro número
# input recebe como texto, float() converte para número decimal
num1 = float(input('Digite o primeiro número: '))

# pede o segundo número
# também converte para número decimal
num2 = float(input('Digite o segundo número: '))


# verifica se a opção escolhida foi 1
# == significa "é igual a"
if opcao == 1:
    
    # se for 1, faz a soma dos dois números
    print('A soma é:', num1 + num2)


# se não for 1, o programa testa a próxima condição
# verifica se a opção escolhida foi 2
elif opcao == 2:
    
    # se for 2, faz a subtração
    print('A subtração é:', num1 - num2)


# se não for 1 nem 2, verifica se é 3
elif opcao == 3:
    
    # se for 3, faz a multiplicação
    print('A multiplicação é:', num1 * num2)


# se não for nenhuma das anteriores, verifica se é 4
elif opcao == 4:
    
    # antes de dividir, o programa verifica se o segundo número é diferente de zero
    # != significa "diferente de"
    if num2 != 0:
        
        # se num2 for diferente de 0, pode fazer a divisão normalmente
        print('A divisão é:', num1 / num2)
    
    else:
        
        # se num2 for 0, mostra um erro porque não existe divisão por zero
        print('Erro: Divisão por zero não é permitida.')


# se nenhuma opção válida for escolhida
else:
    
    # o programa informa que a opção digitada não existe
    print('Opção inválida')
































 





