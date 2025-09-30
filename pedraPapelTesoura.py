import random

lista = ["pedra", "papel", "tesoura"]

while True:
    pergunta = input("Pedra, Papel ou Tesoura (q - quit): ").lower()

    if pergunta == "q":
        print("Jogo encerrado.")
        break

    sorteio = random.choice(lista)

    if (sorteio == "pedra" and pergunta == "papel") or \
       (sorteio == "papel" and pergunta == "tesoura") or \
       (sorteio == "tesoura" and pergunta == "pedra"):
        print("Ganhaste!")
    elif sorteio == pergunta:
        print("Empate!")
    else:
        print("Perdeste!")

    print(f"O computador escolheu: {sorteio}")
