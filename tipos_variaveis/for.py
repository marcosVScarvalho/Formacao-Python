print("For utilizando lista")
lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)

print("\nFor utilizando tupla")
tupla = (1,2,3,4,5)
for elemento in tupla:
    print(elemento)

print("\nFor utilizando chaves")
pessoa = {"nome": "Marcos", "idade": 19, "cidade": "Brasilia-df"}
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)

print("\nFor utilizando o dicionario - items")
for chave,valor in pessoa.items():
    print(f"{chave} : {valor}")

# range(): intervalo numerico
#[0,1,2,3,4,5,6,7,8,9]
print("\nUtilizando a função range()")
for numero in range(5):
    print("Numero: ", numero)

print("\nUtilizando a função range() com len()")
lista = [1,2,3,4,5,6,7,8]
print(lista)
for indice in range(0, len(lista)):
    print("Indice : ", indice)
    print("Elemento : ", lista[indice])
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
    print(lista)

#enumerate()
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Indice 1")