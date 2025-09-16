#instrução condicional

idade = int(input("qual é a tua idade: "))

if idade < 18:
    print("menor de idade")
elif idade == 18:
    print("acabaste e fazer 18")
else:
    print("maior de idade")
