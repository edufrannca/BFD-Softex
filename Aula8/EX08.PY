'''Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
uma função chamada atualizar_perfil que receba um dicionário de perfil de 
usuário e kwargs com as informações a serem atualizadas. A função deve 
retornar o dicionário atualizado. 
Exemplo: perfil = {'nome': 'João', 'idade': 30} e atualizar_perfil(perfil, 
idade=31, cidade="Rio de Janeiro")'''

def atualizar_perfil(perfil, **kwargs):
    perfil.update(kwargs)
    return perfil

perfil = {'nome': 'João', 'idade': 30}
print(atualizar_perfil(perfil, idade=31, cidade="Rio de Janeiro"))