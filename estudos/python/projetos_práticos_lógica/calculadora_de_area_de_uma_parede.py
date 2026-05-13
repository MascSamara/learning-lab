largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura

# cada litro de tinta pinta 2 metros quadrados, então dividimos a área por 2 para saber quantos litros de tinta precisamos.
tinta = area / 2
print(' A área da parede é:', area, ' metros quadrados.')
print(f'Precisa-se de {tinta:.1f} litros de tinta para pintar a parede.')

