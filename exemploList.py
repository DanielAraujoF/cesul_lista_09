# 14 de jun de 2023
lista = ["0 - daniel", "1 - joao", "2 - matheus"]
lista_vazia = []
print('- - - - -')

# mostra a lista completa
print(lista)
print('- - - - -')

# mostra apenas um dos elementos da lista
print(lista[1])
print('- - - - -')

# ex01 - .append adiciona um novo elemento na lista já existente
lista_vazia = lista_vazia.append("3 - lucas")
print(lista_vazia)
print('- - - - -')

# ex02 - .pop remove um elemento da lista já existente
lista_vazia.pop(3)
print(lista)
print('- - - - -')

# mostra quantos elementos tem na lista atualmente
print(len(lista_vazia))
print('- - - - -')

# cria um range do tamanho da lista usando a variável i como índice (posição de cada elemento
for i in range(len(lista)):
    print(lista[i])
print('- - - - -')

# for que atribui à variável à cada elemento na lista
for l in lista:
    print(l)
print('- - - - -')

# for que mostra a posição de cada elemento na lista
for i, p in enumerate(lista):
    print(f"Nome: {p} | Na posição: {i}")

