'''Crie um arquivo .py e peça para o usuário inserir dois valores numéricos (podem ser inteiros 
ou decimais). Armazene-os nas variáveis num1 e num2. Crie uma variável 
MULTIPLICACAO e atribua a ela o valor da multiplicação entre num1 e num2, além disso 
crie uma variável DIVISAO e atribuir a ela o valor da divisão de num1 por num2. Mostre o 
resultado na tela no formato "num1 * num2 = resultado".'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
MULTIPLICACAO = num1 * num2
DIVISAO = num1 / num2
print(f"{num1} * {num2} = {MULTIPLICACAO}")
print(f"{num1} / {num2} = {DIVISAO}")
