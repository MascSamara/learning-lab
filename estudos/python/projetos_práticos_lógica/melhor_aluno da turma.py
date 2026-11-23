# Programa que recebe o nome e a nota de cada aluno de uma turma e retorna o nome do aluno com a maior nota.
print("------ESCOLA SANTA PACIÊNCIA------")
nota_maior = 0
nome_com_maior_nota = ""

alunos = int(input("Quantos alunos a turma tem? "))
for sequencia_alunos in range(1, alunos + 1):

    print(f"\nAluno {sequencia_alunos}")
    nome_aluno = input("Nome do aluno: ")
    nota_aluno = float(input("Nota do aluno: "))
    if nota_aluno > nota_maior:
        nota_maior = nota_aluno
        nome_com_maior_nota = nome_aluno

print(f"\n O melhor aproveitamento foi o de {nome_com_maior_nota} com nota {nota_maior}.")
