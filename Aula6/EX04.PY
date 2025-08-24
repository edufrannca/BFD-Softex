'''Crie um arquivo Python (.py) que funcione como uma calculadora. O programa deve pedir 
ao usuário dois números inteiros e um operador aritmético (+, -, *, /, //, %). Em seguida, 
utilize uma estrutura condicional para verificar qual operador foi inserido e realizar a 
operação matemática correspondente. Por fim, exiba o resultado na tela de forma clara. 
Obs: Utilize a função input() para solicitar os valores ao usuário. Além disso, lembre-se de 
utilizar as funções de conversão int() ou float() para converter o valor de texto para 
numérico.'''

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op = input('Digite o operador (+, -, *, /, //, %): ')

if op == '+':
    resultado = n1 + n2
elif op == '-':
    resultado = n1 - n2
elif op == '*':
    resultado = n1 * n2
elif op == '/':
    resultado = n1 / n2
elif op == '//':
    resultado = n1 // n2
elif op == '%':
    resultado = n1 % n2
else:
    resultado = "Operador inválido."

print("Resultado:", resultado)
