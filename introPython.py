#instrução condicional

idade = int(input("qual é a tua idade: "))

if idade < 18:
    print("menor de idade")
elif idade == 18:
    print("acabaste e fazer 18")
else:
    print("maior de idade")

#operadores aritemétricos
altura = 170

print(idade + 5)
print(altura * 2)
print(idade / 2)
print(altura - 2)


#operadores de comparação 

nome = "joao"
estudante = True

print(idade > 18)
print(idade == 18)
print(idade != 18)
print(idade <= 18)
print(idade >= 18)
print(idade < 18)
print(idade >= 18 and nome)
print(idade >= 18 or estudante)
print(not estudante)
