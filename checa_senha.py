# Exemplo de utilização do while

senha_correta = "python123"
senha = ""
while senha != senha_correta:
    senha = input("Digite a senha: ")
    if senha != senha_correta:
        print("Senha incorreta, tente novamente.")
        print("Senha correta! Acesso concedido.")
