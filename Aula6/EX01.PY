'''Passo01: Crie um arquivo Python (.py) e defina a constante IDADE_MINIMA com o valor 
18. Em seguida, peça ao usuário que digite sua idade, armazenando-a na variável 
idade_usuario. Por fim, use uma estrutura condicional if  para comparar a idade do usuário 
com a constante e exibir a mensagem "O usuário é maior de idade.” 
Obs: Utilize a função input() para solicitar a idade ao usuário e lembre-se de fazer a 
conversão do valor recebido para o tipo int(), use a função print() para mostrar na tela a 
mensagem final e utilize as condicionais IF e os operadores do python. 
 
● variavel_inteira = int(input("Digite um valor: ")) 
● variavel_decimal = float(input("Digite outro valor: ")) 
 
Passo02: Utilize o arquivo Python (.py) criado anteriormente e adicione uma estrutura 
condicional elif para comparar a idade do usuário com a constante e exibir a mensagem "O 
usuário é menor e tem 16 ou 17 anos". 
Obs:  Use a função print() para mostrar na tela a mensagem final e utilize as condicionais 
elif e os operadores do python. 
 
Passo03: Utilize o arquivo Python (.py) criado anteriormente e adicione uma estrutura 
condicional else para exibir a mensagem "O usuário é menor de idade". 
Obs: Use a função print() para mostrar na tela a mensagem final e utilize as condicionais 
else e os operadores do python.'''

IDADE_MINIMA = 18 
idade_usuario = int(input("Digite sua idade: "))

if idade_usuario >= IDADE_MINIMA:
    print("O usuário é maior de idade.")
elif idade_usuario >= 16:
    print("O usuário é menor e tem 16 ou 17 anos.")
else:
    print("O usuário é menor de idade.")