'''Crie um arquivo .py. Comece declarando uma variável estoque com o valor 50 e uma 
variável valor, que receberá um número informado pelo usuário. O valor atribuído à variável 
valor deve ser usado para atualizar a variável estoque, aumentando a quantidade em 
estoque. Utilize o operador de atribuição de adição (+=) para atualizar a quantidade em 
estoque. Mostre o novo valor na tela seguindo a estrutura: "Estoque inicial: resultado" e 
"Estoque final: resultado".'''

estoque = 50
valor = int(input("Informe um valor para adicionar ao estoque: "))
print(f"Estoque inicial: {estoque}")
estoque += valor
print(f"Estoque final: {estoque}")
