entrence = ["Mateus", "Gonçalo", "João", "Joana"]

name = input("Qual é o teu nome? ")

idade = int(input("Qual é a tua idade? "))  

if idade < 18:
    print("És menor de idade, não tens acesso.")
else:
    if name in entrence:  
        print("Acesso liberado")
    else:
        print("Nome não reconhecido, acesso negado.")

     




