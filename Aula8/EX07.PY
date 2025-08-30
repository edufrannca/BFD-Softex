'''Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
uma função cadastrar_usuario que aceite nome e email como argumentos 
obrigatórios e qualquer outra informação como kwargs. Imprima todos os 
dados recebidos. 
Exemplo de uso: cadastrar_usuario(nome="Ana", email="ana@email.com", 
idade=30, cidade="Salvador") '''

def cadastrar_usuario(nome, email, **kwargs):
    usuario = {
        "nome": nome,
        "email": email,
        **kwargs
    }
    for chave, valor in usuario.items():
        print(f"{chave}: {valor}")

print("Cadastro 1:")
cadastrar_usuario(nome="Ana", email="ana@email.com", idade=30, cidade="Salvador")
