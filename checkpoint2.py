import re
import funcoes

emailsVazados = {}

resp = "N"
while resp == "N":
    print("\nMenu de opções: \n")
    print("Digite 1 para cadastrar um vazamento.")
    print("Digite 2 para buscar um e-mail (requer o ID).")
    print("Digite 3 para listar os e-mails vazados.")
    print("Digite 4 para sair.")

    opcao = int(input("\nInforme a opção desejada: "))
    if opcao == 1:
        funcoes.cadastrarElemento(emailsVazados)
    elif opcao == 2:
        funcoes.buscarElemento(emailsVazados)
    elif opcao == 3:
        funcoes.exibirElemento(emailsVazados)
    elif opcao == 4:
         resp = input("Deseja mesmo sair? S ou N: ").upper()
    else:
        print ("Opção inválida. Digite novamente.")

print("Obrigado por utilizar nossa plataforma.")