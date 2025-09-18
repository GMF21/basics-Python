entrence = ["Mateus", "Gonçalo", "João", "Joana"]

name = input(("Qual é o teu nome? "))

idade = input(("Qual é a tua idade? "))

for y in entrence:
    if idade < 18:
        print("és menor de idade, não tens acesso.")
        break
    elif name == entrence[0:3]:
        print("Acesso liberado")
     




