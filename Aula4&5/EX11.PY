'''Crie um arquivo .py. Escreva um programa que receba do usuário a quantidade de Km 
percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

carro_alugado = float(input('Quantos Km foram percorridos com o carro alugado? '))
dias_alugado = int(input('Quantos dias o carro foi alugado? '))
preco = (dias_alugado * 60) + (carro_alugado * 0.15)
print(f'O total a pagar é R${preco:.2f}')