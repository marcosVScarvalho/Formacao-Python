print("Exemplo de importação de um módulo Padrão: ")
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")

print("\n Exemplo de criação e utilização de um módulo personalizado")

from meu_modulo import saudacao,dobro

mensagem = saudacao("Gabriel")
resultado_dobro = dobro(5)
print(mensagem)
print(F"O dobro de 5 é {resultado_dobro}")

