nascimento = int(input('Qual ano você nasceu?'))
ano_atual = int(input('Em Qual ano estamos? '))
dia_nascimento = int(input('Em qual dia você nasceu?'))
dia_atual = int(input('Qual o dia atual?'))
mês = int(input('Em Qual mês você nasceu? '))
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mês_atual = int(input('Qual mês atual?'))
idade = ano_atual - nascimento
if mês < mês_atual:
    print(f'Você tem {idade} anos em {ano_atual}')
elif mês == mês_atual and dia_nascimento <= dia_atual:
    print(f'Você tem {idade} anos em {ano_atual}')
else:
    print(f'Você ainda completará {idade} anos em {ano_atual}')

















