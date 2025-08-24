'''Passo01: Crie um arquivo Python (.py) e defina a constante NOTA_MINIMA com o valor 
7.0. Em seguida, peça ao usuário que digite a sua nota final, armazenando-a na variável 
nota_final. Use uma estrutura condicional if para comparar a nota do aluno com a constante 
e exibir a mensagem "Aprovado!". 
Obs: Utilize a função input() para solicitar a nota ao usuário e lembre-se de fazer a 
conversão do valor recebido para o tipo numérico (float), use a função print() para mostrar 
na tela a mensagem final e utilize a condicional IF para criar o primeiro fluxo do programa, 
comparando a nota_final com a NOTA_MINIMA. 
 
Passo02: Utilize o arquivo Python (.py) criado anteriormente e adicione uma estrutura 
condicional elif para exibir a mensagem "O usuário é menor de idade". 
Obs: Use a função print() para mostrar na tela a mensagem final. 
 
Passo03: Utilize o arquivo Python (.py) criado anteriormente e adicione uma estrutura 
condicional else para comparar a nota do aluno com a constante e exibir a mensagem 
"Reprovado!". 
Obs: Use a função print() para mostrar na tela a mensagem final.'''

NOTA_MINIMA = 7.0
nota_final = float(input("Digite sua nota final: "))

if nota_final >= NOTA_MINIMA:
    print("Aprovado!")
elif nota_final >= 5.0:
    print("Recuperação!")
else:
    print("Reprovado!")