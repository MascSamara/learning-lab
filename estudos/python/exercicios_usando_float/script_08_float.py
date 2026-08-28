# creuza 04
# Pergunta ao usuário qual é a temperatura
# input() recebe o valor digitado como TEXTO
# float() converte esse texto para número decimal (para permitir cálculos)
temperatura = float(input("Qual a temperatura em fahrenheit? "))

# Converte a temperatura de Fahrenheit para Celsius
# Fórmula: (F - 32) / 1.8
# Primeiro subtrai 32 da temperatura digitada
# Depois divide por 1.8 para obter o valor em Celsius
c = (temperatura - 32) / 1.8

# Mostra o resultado na tela
# f"" permite inserir variáveis dentro do texto
# {c:.2f} formata o número para mostrar apenas 2 casas decimais
print(f"no brasil estaria {c:.2f}")

celsus = float(input('Qual a temperatura em celsius(Brasil)? '))
# Converte a temperatura de Celsius para Fahrenheit
# Fórmula: (C * 1.8) + 32
f = (celsus * 1.8) + 32
print(f"Em Fahrenheit seria {f:.2f}")
