'''Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
uma função chamada buscar_livro que aceite um título obrigatório e kwargs 
como filtros de busca (por exemplo, autor="Machado de Assis", ano=1899). 
Imprima o título e todos os filtros aplicados.'''

def buscar_livro(titulo, **kwargs):
    print(f"Buscando livro: {titulo}")
    for chave, valor in kwargs.items():
        print(f"Filtro - {chave}: {valor}")

print("Exemplo de busca de livro:")
buscar_livro("Dom Casmurro", autor="Machado de Assis", ano=1899)
