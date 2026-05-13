metros = float(input("Digite o valor em metros:"))
centimetros = metros * 100
milimetros = metros * 1000
kilometro = metros / 1000
ekilometro = metros / 1000000
decimetro = metros * 10
decametro = metros / 10


print(
    f"{metros:.2f} metros equivalem a {centimetros:.2f} centímetros"
    f" e  {milimetros:.2f} milímetros. Já os kilometros equivalem a {kilometro:.2f} km e {ekilometro:.2f} ekm(ekilometro),\n e os decímetros equivalem a {decimetro:.2f} dm e decâmetros equivalem a {decametro:.2f} dam."
)
