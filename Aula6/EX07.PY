'''Crie um arquivo Python (.py) para um programa que simule o rastreamento do status de um 
pedido online. O programa deve solicitar ao usuário que digite o status atual do pedido 
(como "recebido", "em_preparação", "em_entrega" ou "entregue"). Em seguida, utilize a 
estrutura match case para verificar o texto inserido e exibir uma mensagem correspondente 
ao status do pedido. Caso o usuário digite um status não previsto, o programa deve exibir 
uma mensagem informando que o status não foi identificado. 
Obs: Utilize a função input() para receber o texto do status do usuário, e a função print() 
para exibir a mensagem final.'''

status = input("Digite o status do pedido (recebido, em_preparação, em_entrega, entregue): ")

match status:
    case "recebido":
        print("Seu pedido foi recebido.")
    case "em_preparação":
        print("Seu pedido está em preparação.")
    case "em_entrega":
        print("Seu pedido está em entrega.")
    case "entregue":
        print("Seu pedido foi entregue.")
    case _:
        print("Status do pedido não identificado.")
