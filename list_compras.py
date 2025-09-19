lista = ["Água", "Fruta", "carne"]

add = input(str("Adiciona um novo produto: "))

lista.append(add) #funcao para adicionar no array

quantidade = len(lista) #para saber o tamanho

print(f"quantidade de produtos {quantidade} :")

x = ", ".join(lista) #junta tudo
print(x)


