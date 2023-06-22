from random import randint

numeros = []

# for i in range(10):
#     num = int(input("Insira um número inteiro: "))
#     numeros.append(num)

for i in range(10):
    numeros.append(randint(0, 100))

print(numeros)

for i in range(0, len(numeros), 2):
    print(numeros[i])