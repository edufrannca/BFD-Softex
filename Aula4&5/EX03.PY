'''Crie um arquivo .py.Escreva um código que receba do usuário quanto ele ganha por hora 
e o número de horas que ele trabalha no mês, armazenando esses valores em duas 
variáveis diferentes. Calcule e mostre na tela o total do salário do usuário no referido mês. '''

horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
valor_por_hora = float(input("Digite o valor que você ganha por hora: "))

salario = horas_trabalhadas * valor_por_hora

print("O salário total do usuário no mês é:", salario)