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

# laços de repetição

for i in range(0,10,2):
    print("repetição", i)


i=0
while i <= 10:
    print("repetição", i)
    i += 2


# funções (quando utilizando funções chama se programação funcional)

def repetir():
    i=0
    while i <= 10:
        print("repetição", i)
        i += 2
    return

repetir()

#função com parametros
def repetirVezes(vezes):
    i=0
    while i <= 10:
        print("repetição", i)
        i += 2
    return

repetirVezes(5)
    
