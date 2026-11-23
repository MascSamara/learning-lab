print("---- SELETOR DE PESSOAS ----")

# Contadores dos critérios
homens_maiores = 0
homens_castanhos = 0

mulheres_idade = 0
mulheres_loiras = 0

# Lista para armazenar os candidatos
candidatos = []

while True:

    sexo = input("Digite o sexo (M/F) ou S para sair: ").strip().upper()

    if sexo == "S":
        break

    idade = int(input("Qual a sua idade: "))

    cabelo = input(
        "Qual a cor do seu cabelo?\n"
        "[1] Preto\n"
        "[2] Castanho\n"
        "[3] Loiro\n"
        "[4] Ruivo\n"
        "[5] Outro\n"
        "Digite a opção: "
    ).strip()

    # Armazena os dados de cada candidato
    candidatos.append([sexo, idade, cabelo])

    # Verifica os critérios masculinos
    if sexo == "M" and idade > 18:
        homens_maiores += 1

        if cabelo == "2":
            homens_castanhos += 1

    # Verifica os critérios femininos
    elif sexo == "F" and 25 <= idade <= 30:
        mulheres_idade += 1

        if cabelo == "3":
            mulheres_loiras += 1


# Apresenta todos os candidatos cadastrados
print("\n---- CANDIDATOS CADASTRADOS ----")

for pessoa in candidatos:

    sexo, idade, cabelo = pessoa

    if cabelo == "1":
        cor = "Preto"
    elif cabelo == "2":
        cor = "Castanho"
    elif cabelo == "3":
        cor = "Loiro"
    elif cabelo == "4":
        cor = "Ruivo"
    else:
        cor = "Outro"

    print(f"Sexo: {sexo} | Idade: {idade} | Cabelo: {cor}")


# Apresenta o resultado da seleção
print("\n---- RESULTADO DA SELEÇÃO ----")

print(f"Homens maiores de 18 anos: {homens_maiores}")
print(f"Entre eles, com cabelo castanho: {homens_castanhos}")

print(f"Mulheres entre 25 e 30 anos: {mulheres_idade}")
print(f"Entre elas, com cabelo loiro: {mulheres_loiras}")
