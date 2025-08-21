'''Crie um arquivo .py. Comece declarando uma variável numero com o valor 2 e uma variável 
expoente, que receberá um valor numérico informado pelo usuário. O valor atribuído à 
variável expoente deve ser usado para atualizar a variável numero, elevando-o a essa 
potência. Utilize o operador de atribuição de potência (**=) para realizar essa operação. 
Mostre o valor inicial de numero e o valor final na tela.'''

numero = 2
expoente = int(input("Informe um valor para o expoente: "))
print(f"Valor inicial de numero: {numero}")
numero **= expoente
print(f"Valor final de numero: {numero}")
