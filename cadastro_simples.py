print("***Nossa função de cadastro de usuários***")

nome = str(input("Digite o nome e o sobrenome do usuario: "))
cpf = str(input("Informe o CPF: "))
rg = str(input("Informe o RG:"))
estado_civil = str(input("Informe o estado civil:"))

print("Cadastrando o usuario no sistema...")
print("O usuario", nome, "com os dados de CPF:", cpf +
      " RG: " + rg + " Estado Civil: " + estado_civil,
      "foi cadastrado com sucesso!" )