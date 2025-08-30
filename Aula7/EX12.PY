'''Crie um arquivo .py . Escreva um código que vai conter uma variável que vai 
armazenar alguma frase qualquer. Seu objetivo é contar o número de 
palavras únicas na frase fornecida.  
Obs: Você pode utilizar os conceitos de lista e conjunto para concluir esse 
objetivo. Além disso, você pode utilizar a função split() para dividir uma 
string em frases.'''

frase = "Esta é uma frase de exemplo. Esta frase contém palavras repetidas."
palavras = frase.split()
palavras_unicas = set(palavras)
numero_palavras_unicas = len(palavras_unicas)

print("Número de palavras únicas:", numero_palavras_unicas)