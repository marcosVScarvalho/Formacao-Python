# if , elif, else

# Exemplo de "if"
idade = int(input("Quantos anos voce tem ? "))
print("Exemplo de comando IF : ")
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é um adolescente")
else:
    print("Voce é menor de idade")

mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Não pode tirar carteira de habilitação"
print(mensagem)
