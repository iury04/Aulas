# username = "Iuryac"
# password = 200226

# login_username = input("Digite seu usuário:  ")
# login_password = int(input("Digite sua senha: "))

# if login_username == username and login_password == password:
#     print("Acesso concedido! ")
# else:
#     print("Acesso negado! ")

# print("Vamos cadastrar seu documento! ")
# rg = input("Digite seu RG: ")
# cpf = input("Digite seu CPF: ")

# if rg != "" or cpf != "":
#     print("Documentação cadastrada com sucesso.")
# else:
#     print("Preencha o RG ou CPF.")


idade = int(input("Qual é a sua idade? "))

documento = input("Possui documento? sim/não: ")
acompanhado = input("Está acompanhado? sim/não ")

if idade >= 18 and (documento == "sim" or acompanhado == "sim"):
    print("Pode participar! ")
else:
    print("Não pode participar! ")