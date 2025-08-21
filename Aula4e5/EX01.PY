'''Crie um arquivo .py e peça para o usuário inserir dois valores inteiros. Armazene-os nas 
variáveis num1 e num2. Crie uma variável SOMA e atribua a ela o valor da soma de num1 
por num2, além disso crie uma variável SUBTRACAO e atribua a ela o valor da subtração 
de num1 por num2. Mostre os resultados na tela no formato "num1 + num2 = resultado" e 
"num1 - num2 = resultado.'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
SOMA = num1 + num2
SUBTRACAO = num1 - num2
print(f"{num1} + {num2} = {SOMA}")
print(f"{num1} - {num2} = {SUBTRACAO}") 