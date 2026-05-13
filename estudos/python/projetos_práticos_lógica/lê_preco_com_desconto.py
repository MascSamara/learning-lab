valorproduto = float(input('Digite o valor do produto:'))
desconto = 5 / 100
valorcomdesconto = valorproduto - (valorproduto * desconto)
print(f'O valor do produto com desconto é: R$ {valorcomdesconto:.2f}')