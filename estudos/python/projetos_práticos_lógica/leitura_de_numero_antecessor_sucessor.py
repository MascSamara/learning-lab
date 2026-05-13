# Mostra os números antecessor e sucessor de um número digitado, além do dobro, triplo e raiz quadrada:
numero =  (int(input('Digite um número:')))
antessor = numero -1
sucessor = numero +1
dobro= numero * 2
triplo = numero * 3
raizquadrada = numero ** 0.5
print('O múmero digitado foi:', numero, 'O seu antecessor é:', antessor,'e o sucessor é:', sucessor)
print('O dobro do número é:', dobro)
print('O triplo do número é:', triplo)
print('A raiz quadrada do número é: {:3.2f}'.format(raizquadrada))