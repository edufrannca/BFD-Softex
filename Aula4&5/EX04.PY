'''Crie um arquivo .py. Escreva um código, crie uma variável chamada media, defina a ela 
um valor numérico de sua preferência, e crie outra chamada possui_presenca, que deve 
ser definida com o valor True. Em seguida, utilize o operador lógico and para verificar se o 
estudante possui uma média maior ou igual a 7.0 e se também tem presença mínima, 
armazenando o resultado dessa verificação em uma variável chamada elegivel_bolsa. 
Por fim, exiba na tela a mensagem "Elegível para bolsa de estudos? resultado 
da operação lógica", substituindo pelo valor contido em elegivel_bolsa, utilizando 
a função print().'''


aluno = float(input("Qual foi a sua média? "))
possui_presenca = True
elegivel_bolsa = aluno >= 7 and possui_presenca
print("Elegível para bolsa de estudos?", elegivel_bolsa)