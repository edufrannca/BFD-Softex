'''Crie um arquivo .py utilizando o vscode e Replique o código do programa abaixo, rode ele 
no seu vscode e verifique onde está o erro, ao encontrar o erro, conserte-o. 
Obs: Lembre-se de quais são os operadores lógicos e como eles devem ser utilizados. 
Código: 
idade_motorista = int(input("Qual a sua idade? ")) 
tem_carteira = bool(input("Você tem carteira de motorista? (True/False) ")) 
pode_dirigir = idade_motorista > 18 or tem_carteira == True 
print(f"Pode dirigir? {pode_dirigir}") 
Saída esperada: 
Pode dirigir? True'''

idade_motorista = int(input("Qual a sua idade? ")) 
resposta = input("Você tem carteira de motorista? (True/False) ")
tem_carteira = resposta.lower() == "true"
pode_dirigir = idade_motorista >= 18 and tem_carteira
print(f"Pode dirigir? {pode_dirigir}")