usuarios = []

def menu():
    print("\n=== SISTEMA DE CADASTRO ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Buscar usuário")
    print("4 - Deletar usuário")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))

        usuario = {
            "nome": nome,
            "idade": idade
        }

        usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        if not usuarios:
            print("Nenhum usuario cadastrado!")
        else:
            print(usuarios)

    elif opcao == "3":
        nome_busca = input("Digite o nome do usuário: ")
        
        for usuario in usuarios:
            if usuario["nome"] == nome_busca:
                print(f"Usuário encontrado: {usuario}")
                break
        else:
            print("Usuário não encontrado.")

    elif opcao == "0":
        print("Saindo do sistema...")
        break
    
    elif opcao == "4":
        nome_remove = input("Digite o nome do usuário que deseja remover: ")

        for usuario in usuarios:
            if usuario["nome"] == nome_remove:
                usuarios.remove(usuario)
                print(f"Usuário removido com sucesso! {usuario}")
                break
        else:
            print("Usuário não encontrado!")