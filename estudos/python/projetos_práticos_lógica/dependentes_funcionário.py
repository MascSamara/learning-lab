nome = input('Qual o nome do funcionário(a)? ')
salario = float(input('Qual o salário do funcionário(a)? R$ '))
dependentes = int(input('Quantos dependentes o funcionário(a) possui? '))
novo_salario = dependentes
if novo_salario <= salario + (salario*5/100):
    print(f'O funcionário(a) {nome} terá um aumento de 5% no salário.')
    novo_salario = salario + (salario*5/100)
elif novo_salario <= salario + (salario*10/100):
    print(f'O funcionário {nome} terá um aumento de 10% no salário.')
    novo_salario = salario + (salario*10/100)
elif novo_salario <= salario + (salario*15/100):
    print(f'O funcionário {nome} terá um aumento de 15% no salário.')
    novo_salario = salario + (salario*15/100)
elif novo_salario > salario + (salario*18/100):
    print(f'O funcionário {nome} terá um aumento de 18% no salário.')
    novo_salario = salario + (salario*18/100)
print(f'O novo salário de {nome} será de R$ {novo_salario:.2f}.')



