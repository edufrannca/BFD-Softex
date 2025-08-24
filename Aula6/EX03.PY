'''Crie um arquivo Python (.py) e solicite ao usuário que digite três números inteiros, 
armazenando-os em variáveis separadas. Em seguida, utilize estruturas condicionais(IF, 
ELSE e ELIF) para exibir os números na tela em ordem decrescente. 
Obs: Utilize a função input() para solicitar os valores ao usuário. Além disso, lembre-se de 
utilizar as funções de conversão int() ou float() para converter o valor de texto para 
numérico.'''

N1 = int(input('Digite o primeiro número: '))
N2 = int(input('Digite o segundo número: '))
N3 = int(input('Digite o terceiro número: '))

if N1 >= N2 and N1 >= N3:
    maior = N1
    if N2 >= N3:
        menor = N3
    else:
        menor = N2
elif N2 >= N1 and N2 >= N3:
    maior = N2
    if N1 >= N3:
        menor = N3
    else:
        menor = N1
else:
    maior = N3
    if N1 >= N2:
        menor = N2
    else:
        menor = N1

print("Ordem decrescente:", maior, menor)