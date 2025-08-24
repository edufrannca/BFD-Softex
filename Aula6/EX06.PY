'''Para realizar este exercício, crie um arquivo Python (.py) onde o programa irá solicitar ao 
usuário uma nota de 1 a 5. Em seguida, utilize a estrutura de controle de fluxo match case 
para comparar a nota fornecida com cada caso possível, exibindo um feedback 
correspondente. Se a nota estiver fora do intervalo de 1 a 5, o caso padrão (_) deverá ser 
usado para exibir uma mensagem de erro. 
Obs: Utilize a função input() para receber a nota do usuário e a função print() para exibir a 
mensagem final. Além disso, lembre-se de utilizar as funções de conversão int() ou float() 
para converter o valor de texto para numérico. '''

nota = int(input("Digite uma nota de 1 a 5: "))

match nota:
    case 1:
        print("Nota muito baixa.")
    case 2:
        print("Nota baixa.")
    case 3:
        print("Nota média.")
    case 4:
        print("Nota alta.")
    case 5:
        print("Nota máxima.")
    case _:
        print("Nota inválida. Digite uma nota de 1 a 5.")
