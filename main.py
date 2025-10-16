# import calculo --- calculo.dobro()
# importando de outro jeito:
from calculo import dobro, triplo, quadrado
from interface import mostra_menu

while True:
    mostra_menu()

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        numero = input("Iniciando cálculo do dobro... Digite o numero: ")
        dobronum = dobro(numero) # chamando a função dobro com o num do usuario
        print(f"O dobro de {numero} é {dobronum}")

    elif opcao == "2":
        numero = input("Iniciando cálculo do triplo... Digite o numero: ")
        triplonum = triplo(numero) # chamando a função triplo com o num do usuario
        print(f"O triplo de {numero} é {triplonum}")

    elif opcao == "3":
        numero = input("Iniciando cálculo do quadrado... Digite o numero: ")
        quadradonum = quadrado(numero) # chamando a função quadrado com o num do usuario
        print(f"O quadrado de {numero} é {quadradonum}")

    elif opcao == "4":
        print("-- ENCERRANDO PROGRAMA... ")
        break

    else :
        print("Opção invalida! \n")
        continue    