'''Crie um arquivo .py. Crie uma variável senha com o valor "Python123". Crie uma variável 
senha_valida e atribua a ela o resultado de uma expressão que verifique as seguintes 
condições (usando os operadores lógicos): 
● A senha não é vazia. 
● A senha tem mais de 8 caracteres. 
● A senha é exatamente igual a "Python123". 
● A senha é diferente de "123456". 
● Combine todas as condições com os operadores and e not e exiba o resultado final.'''

senha = "Python123"
senha_valida = (senha != "") and (len(senha) > 8) and (senha == "Python123") and (senha != "123456")
print(f"Senha válida? {senha_valida}")
