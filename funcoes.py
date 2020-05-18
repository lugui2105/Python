def cadastrarElemento(leak):
    resp = "S"
    while resp == "S":
        tag = input("Digite um ID para cadastrar o e-mail vazado: ").upper()
        leak[tag] = [input("Digite o e-mail que deseja cadastrar: "), input("Digite a senha do e-mail: "), int(input("Digite a validade: "))]
        resp = input("Deseja cadastrar mais um email? S ou N: ").upper()

def buscarElemento(leak):
    busca = input("Digite o ID do e-mail que deseja buscar: ").upper()
    lista = leak.get(busca)
    if lista != None:
        print("\nEmail: ", lista[0])
        print("Senha: ", lista[1])
        print("Validade: ", lista[2])
    else:
        print("Vazamento não encontrado! ")

def exibirElemento(leak):
    for tag, dados in leak.items():
            print("\nID do e-mail: ", tag)
            print("E-mail: ", dados[0])
            print("Senha: ", dados[1])
            print("Validade: ", dados[2])