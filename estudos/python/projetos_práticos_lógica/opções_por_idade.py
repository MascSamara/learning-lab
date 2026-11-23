# Mostrar categorias e capturar escolha
print("-----------Categorias-----------")
print("[1] Aventura")
print("[2] Comédia")
print("[3] Drama")
print("[4] Terror")
print("[5] Suspense")
print("[6] Romance")
print("[7] Ficção científica")
print("[8] Animação")
print("[9] Documentário")

categoria_escolhida = int(input("Qual categoria de filme você deseja assistir? (Digite o número correspondente): "))

# Mapear categoria e idade minima com base no que o usuário escolheu
match categoria_escolhida:
    case 1:
        idade_minima = 12
    case 2:
        idade_minima = 16
    case 3:
        idade_minima = 16
    case 4:
        idade_minima = 18
    case 5:
        idade_minima = 18
    case 6:
        idade_minima = 18
    case 7:
        idade_minima = 18
    case 8:
        idade_minima = 12
    case 9:
        idade_minima = 18
    case _:
        idade_minima = None
        print('Categoria inválida')

# Só continua se a categoria for válida
if idade_minima is not None:
    idade = int(input("Qual é a sua idade? "))

    # Comparação genérica, uma única regra pra qualquer categoria
    if idade >= idade_minima:
        print(f"Liberado! Você pode assistir a categoria escolhida (idade mínima: {idade_minima}).")
    else:
        print(f"Bloqueado. Essa categoria exige idade mínima de {idade_minima} anos.")
            
        