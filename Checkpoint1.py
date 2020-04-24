listaEmails = []
resp = "S"
while resp == "S":
    listaEmails.append(input("Digite o e-mail para adicionar: ").upper())
    respWhile = ""
    while respWhile != "S" and respWhile != "N":
        respWhile = input("Digitar outro e-mail? S para SIM e N para NÃO: ").upper()
    resp = respWhile

email = input("Digite o e-mail para verificar se está na lista: ").upper()
if email in listaEmails:
    print("O e-mail está na lista.")
else:
    print("O e-mail não está na lista.")


