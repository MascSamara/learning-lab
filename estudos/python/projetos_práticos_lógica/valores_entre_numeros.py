#Usuario digita 6 numeros o programa mostra numeros entre 0 e 10.
tot010=0
soma_numeros_impares=0
imp_fora =0
contador=0
valor = 0
print("Digite 6 numeros entre 0 e 10")
for contador in range(1,7):
    valor = int(input("Digite o {}º numero: ".format(contador)))
    if valor >= 0 and valor <= 10:
        tot010 += 1
        if valor % 2 != 0:
            soma_numeros_impares += valor
    else:
        if valor % 2 != 0:
            imp_fora += valor
print("Ao todo foram  {} valores entre 0 e 10.".format(tot010))
print("Nesse intervalo, a soma de ímpares é: {}".format(soma_numeros_impares + imp_fora))



