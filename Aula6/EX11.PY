'''Crie um arquivo .py. Peça ao usuário para inserir um número inteiro. Em seguida, use um 
laço for para exibir a tabuada de multiplicação desse número, de 1 a 10. 
Obs: Crie uma lista de valores numéricos de 1 a 10 ou utilize a função range() para criar 
uma lista de maneira mais rápida. 
range(valor inicial, valor final)     |     lista = [1, 2, 3…10]'''

usuario = int(input("Digite um número: "))

for i in range(1,11):
    print(usuario, "x", i, "=", usuario * i)