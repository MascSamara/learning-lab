                            #CREUZA 01
# Pergunta ao usuário em que ano estamos
# input() mostra a pergunta e espera o usuário digitar algo
# O valor digitado é armazenado na variável "ano"
# Importante: input() sempre retorna TEXTO (string)
ano = input('Em que ano estamos?')

# Pergunta em que ano a pessoa nasceu
# O valor digitado será guardado na variável "nascimento"
# Também será recebido como TEXTO
nascimento = input('Em que ano nasci?')

# int() converte o texto para número inteiro
# Isso é necessário porque não podemos fazer contas com texto
# Aqui o programa faz a conta: ano atual - ano de nascimento
idade = int(ano) - int(nascimento)

# print() mostra uma mensagem na tela
# O f antes das aspas indica uma f-string (string formatada)
# {idade} coloca o valor da variável dentro da frase
print(f"Tenho {idade} anos.")
