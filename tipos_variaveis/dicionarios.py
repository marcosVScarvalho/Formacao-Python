# Criando um dicionario de exemplo 
pessoa = {"nome": "Marcos", "idade": 19, "cidade": "Brasilia - DF"}

# Exibindo o dicionario
print("Meu dicionario de exempo : ", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade: ", pessoa["idade"])
print("Cidade: ", pessoa["cidade"])

pessoa["sobrenome"] = "Vinicius"
print("Sobrenome", pessoa['sobrenome'])
print("Meu dicionario de exempo : ", pessoa)

pessoa['idade'] = 31
print("Idade atualizada: ", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionario de exempo : ", pessoa)

# Métodos: keys(), values(), items()
chaves = list(pessoa.keys())
print("Chaves do dicionario:", chaves)
print("Primeira chave:", chaves[0])

# Método values
valores = list(pessoa.values())
print("Valores do dicionario:", valores)
print("Primeiro valor do dicionario:", valores[0])

# Método items
itens = list(pessoa.items())
print("Pares chave-valor do dicionario: ", itens)
print("Primeira chave-valor : %s = %s" % (itens[0][0], itens[0][1]))