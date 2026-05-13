salarioatual = float(input('Digite o salário atual:'))
aumento = 15/100
salariofinal = salarioatual + (salarioatual * aumento)

print('O salário com aumento é R$ {:.2f}'.format(salariofinal))