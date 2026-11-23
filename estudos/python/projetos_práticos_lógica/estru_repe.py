# Agora criando o while porém o usuário poderá o valor e o programa pergunta se ele deseja continuar caso ele diga sim o programa continua pedindo números e somando, caso ele diga não o programa para e mostra a soma dos números digitados

soma = 0
contador =1

while True:
    numero = float(input(f"Digite o {contador}º número: "))
    soma += numero
    contador += 1
    resposta = input(f"Você deseja continuar somando números? (sim/não): ").lower()
    if resposta != "sim":
        break
print(f"A soma dos números é: {soma}")






