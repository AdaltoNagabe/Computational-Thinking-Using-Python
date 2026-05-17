def exibir_menu():
    print("\n--- MENU ---")
    print("1. Ver perfil")
    print("2. Editar configurações")
    print("3. Ver histórico de escolhas")
    print("0. Sair")


def rodar_menu():
    # 1. Cria a lista vazia para armazenar o histórico de opções
    historico_opcoes = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Você acessou o perfil.")
            # 2. Adiciona a opção à lista
            historico_opcoes.append(1)

        elif opcao == "2":
            print("Você acessou as configurações.")
            historico_opcoes.append(2)

        elif opcao == "3":
            # Mostra o histórico que estamos guardando
            print(f"\nSeu histórico de escolhas até agora: {historico_opcoes}")
            historico_opcoes.append(3)

        elif opcao == "0":
            print("Saindo do programa...")
            # Mostra o histórico final antes de fechar
            print(f"Histórico final de navegação: {historico_opcoes}")
            break

        else:
            print("Opção inválida! Tente novamente.")


# Executa o menu
rodar_menu()