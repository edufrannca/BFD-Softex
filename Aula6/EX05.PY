'''Crie um arquivo Python (.py) para um programa que solicite ao usuário que digite um 
número inteiro de 1 a 7.Com base no número, exiba na tela o dia da semana 
correspondente (1 para domingo, 2 para segunda-feira, e assim por diante). Se o usuário 
digitar um número fora do intervalo de 1 a 7, o programa deve exibir uma mensagem de 
erro. 
Obs: Utilize a função input() para receber o valor do usuário, a função print() para exibir a 
mensagem final e estrutura condicional match para criar os diferentes fluxos do programa. . 
Além disso, lembre-se de utilizar as funções de conversão int() ou float() para converter o 
valor de texto para numérico.'''

usuario = int(input("Digite um número de 1 a 7: "))

match usuario:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-feira")
    case 3:
        print("Terça-feira")
    case 4:
        print("Quarta-feira")
    case 5:
        print("Quinta-feira")
    case 6:
        print("Sexta-feira")
    case 7:
        print("Sábado")
    case _:
        print("Número inválido. Digite um número de 1 a 7.")
