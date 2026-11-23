#........................................................Somador numérico...............................................
# recebe números do usuário enquanto ele desejar continuar e, ao final, exibe os números digitados e a soma.

resposta = "sim"
soma = 0
numeros_digitados = []

# Enquanto(WHILE) é estrtura de erepetição com teste lógico no inicio do código, ou seja, enquanto a condição for verdadeira o bloco de código será executado.
while resposta == "sim":
    numero = int(input("Digite um número: "))
    numeros_digitados.append(numero)
    
#.lower() é um método de strings do Python que transforma todas as letras de um texto em minúsculas.
    resposta = input("Deseja continuar? (sim/não): ").lower() 
    soma = soma + numero
print(f"Os valores digitados foram {numeros_digitados} e a soma deles é {soma}")



