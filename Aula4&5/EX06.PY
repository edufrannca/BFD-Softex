'''Crie um arquivo .py utilizando o vscode e Replique o código do programa abaixo, rode ele 
no seu vscode e verifique onde está o erro, ao encontrar o erro, conserte-o. 
Obs: Lembre-se de como são utilizados os operadores de atribuição matemáticos. 
Código: 
total_cliques = 0  
total_cliques + = 1  
print(f'O total de cliques e de: {total_cliques}') 
total_cliques =+ 1  
print(f'O total de cliques e de: {total_cliques}') 
Saída esperada: 
O total de cliques e de: 1 
O total de cliques e de: 2'''

total_cliques = 0  
total_cliques += 1
print(f'O total de cliques e de: {total_cliques}')
total_cliques += 1
print(f'O total de cliques e de: {total_cliques}')