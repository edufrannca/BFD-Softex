'''Crie um arquivo .py utilizando o vscode e Replique o código do programa abaixo, rode ele 
no seu vscode e verifique onde está o erro, ao encontrar o erro, conserte-o. 
Obs: Lembre-se de quais são os operadores aritméticos e como eles devem ser utilizados. 
Uma observação à expressão da linha 04, espera obter os itens que sobraram da divisão de 
todos os itens para o total de cestas. 
Código: 
total_itens = 25  
total_cestas = 4  
itens_por_cesta = total_itens / / total_cestas 
itens_restantes = total_itens * total_cestas 
print(f"Itens por cesta: {itens_por_cesta}") 
print(f"Itens restantes: {itens_restantes}") 
Saída esperada: 
Itens por cesta: 6  
Itens restantes: 1'''

total_itens = 25  
total_cestas = 4  
itens_por_cesta = total_itens // total_cestas 
itens_restantes = total_itens % total_cestas
print(f"Itens por cesta: {itens_por_cesta}")
print(f"Itens restantes: {itens_restantes}")