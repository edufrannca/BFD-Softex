'''Crie um arquivo .py. Defina uma senha correta, por exemplo, "python123". Peça ao usuário 
para digitar uma senha. Use um laço while que continue pedindo a senha enquanto ela for 
diferente da senha correta. Quando a senha estiver certa, exiba uma mensagem de 
sucesso. 
Obs: Utilize input() para capturar a senha e print() para exibir as mensagens.'''

SENHA = "python123"
senha_usuario = input("Digite a senha: ")

while senha_usuario != SENHA:
    print("Senha incorreta. Tente novamente.")
    senha_usuario = input("Digite a senha: ")

print("Senha correta. Acesso concedido.")