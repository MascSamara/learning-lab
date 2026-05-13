#Clculo IMC
massa= float(input('Massa(Kg): '))
altura = float(input('Altura(m): '))
imc = massa/altura**2
print(' IMC: ', f'{imc:5.2f}')
if (imc >= 18.5) and (imc < 25):
    print('Parabéns!você está no seu peso ideal.')
else:
    print('Você não está na faixa de peso ideal. ')




























