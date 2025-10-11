import calculo

print("ola mundo agora no vscode \n")
print("programa dos calculos")
print("-" * 50)

x = input("Digite o numero e vou dizer o dobro:")

dobro = calculo.dobro(x)

print(f"o dobro de {x} é {dobro}")


y = input("Agora, digite outro numero e vou dizer o triplo")

triplo = calculo.triplo(y)

print(f"O trplo de {y} é {triplo}")