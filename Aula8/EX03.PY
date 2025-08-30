'''Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
uma função que receba um texto qualquer como argumento. A função deve 
retornar a quantidade de vogais (a, e, i, o, u) do valor informado e esse 
resultado deve ser mostrado na tela.'''

def contar_vogais(texto):
    vogais = "aeiou"
    return sum(1 for letra in texto.lower() if letra in vogais)

print(f"A quantidade de vogais é: {contar_vogais('Olá, mundo!')}")
