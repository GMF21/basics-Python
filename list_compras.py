lista = []

def mostrar_quantidade():
    return len(lista)

def mostrar_produtos():
    if len(lista) > 0:
        return ", ".join(lista)
    else:
        return "nenhum produto"

while True:
    quantidade = mostrar_quantidade()
    produtos = mostrar_produtos()

    add = int(input(f"Queres adicionar um produto à tua lista? Atualmente tens {quantidade} na tua lista (1-sim/2-não/3-remover produto): "))

    if quantidade == 0:
        print("Não tens nenhum produto na tua lista")

    if add == 1:
        novo_produto = input("Nome produto: ")
        lista.append(novo_produto)
    elif add == 2:
        print("Não adicionaste nenhum produto. A sair...")
        break
    elif add == 3:
        if mostrar_quantidade() == 0:
            print("Não há nada para remover.")
        else:
            print(f"Produtos disponíveis a remover: {mostrar_produtos()}")
            remover = input("Qual o produto que queres remover da lista: ")
            
            if remover not in lista:
                print(f"Esse produto não está na lista, produtos disponíveis: {mostrar_produtos()}")
            else:
                lista.remove(remover)

print(f"Sua lista tem {mostrar_quantidade()} produtos: {mostrar_produtos()}")
