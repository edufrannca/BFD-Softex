'''Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
uma função calcular_media que aceita qualquer quantidade de notas (*args) 
e retorne a média delas. 
Exemplo de uso: calcular_media(8.5, 9.0, 7.5) deve retornar 8.33. '''

def calcular_media(*args):
    return sum(args) / len(args) if args else 0

print(f"A média é: {calcular_media(8.5, 9.0, 7.5):.2f}")