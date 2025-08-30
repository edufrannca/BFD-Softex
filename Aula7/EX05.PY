'''Crie um arquivo .py. Escreva um código que vai armazenar os seguintes 
dados de uma venda de produto e a quantidade dele  'Caderno', 15 em uma 
tupla chamada venda. Você precisa calcular o valor total da venda, nesse 
caso imagine que o preço unitário do produto é R$ 25,00. Mostre o resultado 
na tela para o usuário.  '''

venda = ('Caderno', 15)
preco_unitario = 25.00
valor_total = venda[1] * preco_unitario
print("Valor total da venda:", valor_total)
