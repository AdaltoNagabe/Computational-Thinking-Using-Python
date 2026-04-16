def exibir_menu():  #Função para exibir o menu
    print("\n--- SISTEMA DE GESTÃO ---")
    print("1. Adicionar Item")
    print("2. Remover Item")
    print("3. Visualizar Relatório")
    print("0. Sair")
    print("-------------------------")
    
# Simulação de estrutura Pós-Condicional (Do-While)
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
 
    match (opcao):
      case "1":
        print(">> Abrindo tela de cadastro...")
      case "2":
        print(">> Abrindo tela de exclusão...")
      case "3":
        print(">> Gerando relatório em PDF...")
      case "0":
        print("Saindo do sistema... Até logo!")
        break
      case _:
        print("Opção inválida! Tente novamente.")