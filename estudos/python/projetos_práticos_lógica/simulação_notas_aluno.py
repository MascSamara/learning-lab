# Calcula a média de um aluno e mostra se ele foi aprovado ou reprovado:
nota1 = float(input('Digite a primeira nota do aluno:'))
nota2 = float(input('Digite a segunda nota do aluno:'))
media = (nota1 + nota2) / 2

print (f' A média do aluno é: {media:.1f}')
if media >= 60:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')

