# Departamento de trânsito:
ano = int(input('Ano atual:'))
nascimento = int(input('Qual seu ano de nascimento?'))
dirigir = ano - nascimento
if dirigir >=18:
        print('Parabéns! Você está apto a dirigir.')
else:
        print('Você não está apto a dirigir pois sua idade é de:', dirigir, 'anos.')
