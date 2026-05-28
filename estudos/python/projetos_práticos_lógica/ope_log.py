# Operador and (e)/ Todas as condições precisam ser verdadeiras:
media = 6
if media >= 5 and media < 7:
    print("Aluno em recuperação")

# Operador or (ou)/ Basta uma condição ser verdadeira:
idade = 18
if idade >= 18 or idade < 25:
    print("Aluno é maior de idade ou está na faixa etária específica")

# Operador not (não)/ inverte o resultado de uma condição:
# NOT significa "não" e inverte o resultado da condição.
# Ele verifica o contrário: se a condição é False, NOT transforma em True(verdadadeiro) 
# se a condição é True, NOT transforma em False(falso).;
# Ex.: tem_permissao = False → not tem_permissao = True
# Ou seja: "não tem permissão?" → Sim → acesso negado.
tem_permissao = False
if not tem_permissao:
    print("Acesso negado")

