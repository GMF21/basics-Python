fruta = ["maçã", "banana", "laranja"]
print(fruta[0])
print(fruta[1])
print(fruta[2])

fruta[0] = "pera"
print(fruta[0])

direito = fruta.sort()

print(direito)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 


x = ["BANANA", "SLA", "NS"]

x[1] = "KIWI"

print(x)

carros = ("BMW", "FERRARI", "Lamborghini")
(marca1, marca2, marca3) = carros

print(marca1)

oMeuSet = frozenset({"a", "b", "c"}) #para congelar n da para adicionar remover nada ta feito ta feito

for carro in carros:
  print(carro)
