import random

lista = ["pedra", "papel", "tesoura"]

contador = 0
perdeste = 0
empate = 0

while True:
    pergunta = input("Pedra, Papel ou Tesoura (q - quit): ").lower()

    if pergunta == "q":
        print("A sair...")
        break

    sorteio = random.choice(lista)

    
    if (sorteio == "pedra" and pergunta == "papel") or \
       (sorteio == "papel" and pergunta == "tesoura") or \
       (sorteio == "tesoura" and pergunta == "pedra"):
        print("win")
        contador += 1
        

    elif sorteio == pergunta:
        print("Empate")
        empate += 1
    else:
        print("Perdeste")
        perdeste += 1

    print(f"O computador escolheu: {sorteio}")

    print(f"Ganhaste {contador} vezes, e perdeste {perdeste} vezes e empataste {empate} vezes")
