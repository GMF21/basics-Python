import random

numeros = list(range(100))

random.shuffle(numeros)


while True:
    

    pergunta = str(input("sortear numero(s/n)"))
   

    if pergunta == "s":

        sorteio = numeros.pop()
        print(f"Num: {sorteio}")
    elif pergunta == "n":
        print("A sair...")
        break
    else:
        print("Mete 's'para sim 'n' para sair ")








    






