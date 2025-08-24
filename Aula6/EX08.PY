'''Para este exercício, crie um arquivo Python (.py) onde o programa irá solicitar ao usuário 
que digite a cor de um semáforo ("verde", "amarelo" ou "vermelho"). Em seguida, utilize a 
estrutura match case para verificar a cor e exibir a ação correspondente que um motorista 
deve tomar. Caso a entrada não seja nenhuma das cores válidas, o programa deve informar 
que o sinal está inválido. 
Obs: Use a função input() para receber a cor do semáforo do usuário e print() para exibir a 
mensagem final. '''

semaforo = input("Digite a cor do semáforo (verde, amarelo, vermelho): ")

match semaforo:
    case "verde":
        print("Siga em frente.")
    case "amarelo":
        print("Atenção! Prepare-se para parar.")
    case "vermelho":
        print("Pare!")
    case _:
        print("Sinal inválido.")
