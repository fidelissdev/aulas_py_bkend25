# import calculo
# importando de outro jeito:
from calculo import dobro, triplo

print("ola mundo agora no vscode \n")
print("programa dos calculos")
print("-" * 50)

x = input("Digite o numero e vou dizer o dobro:")

dobro = dobro(x)

print(f"o dobro de {x} é {dobro}")


y = input("Agora, digite outro numero e vou dizer o triplo")

triplo = triplo(y)

print(f"O trplo de {y} é {triplo}")