# Lê um número e mostra a tabuda desse número:
numero = int(input('Digite um número:'))
#for é estrutura de repetição
# i é uma variável de controle, que vai assumir os valores de 1 a 10, colocamos 11 pois o ultimo valor não é incluído
# in é usado para indicar que a variável de controle vai assumir os valores de uma sequência, no caso a função range.
# range é uma função que gera uma sequência de números, no caso de 1 a 10.
for i in range(1, 11):
# f é usado para formatar a string, permitindo inserir variáveis dentro da string de forma mais fácil e legível.
# {} é usado pra indicar onde a variável deve ser inserida na string.
# x é o simbolo de multiplicação, e o resultado da multiplicação é mostrada aos usuários.   
    print(f'{numero} x {i} = {numero * i}')