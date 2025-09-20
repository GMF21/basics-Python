lista = ["forno", "fogão", "água"]

try:

    add = int(input("queres adicionar um novo produto a tua lista? (1-sim/2-não)"))
except ValueError:
    print("Digita 1 para adicionar e 2 para não")

if add == 1:
    produto = input(str("Nome do produto: "))
    lista.append(produto)
elif add == 2:
    print("não adicionaste nenhum produto a mais")
    

quantidade = len(lista)
x = ", ".join(lista)

print(f"Tens {quantidade} na tua lista: {x}")

