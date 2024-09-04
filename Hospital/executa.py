from menu import* 
from paciente import*
from funcionario import*
from vacina import*

banco_de_dados = 'Hospital/banco_de_dados.json'

menu = Menu()
paciente = Paciente()
funcionario = Funcionario()
vacina = Vacina()

while (True):
    menu.menuInicial()
    try:
        opcao_menu = int(input(">>> "))

        #Escolha Paciente
        if opcao_menu == 1:
            menu.menu_paciente()
            while (True):
                try:
                    op_paciente = int(input(">>> "))

                    if op_paciente == 1:
                        paciente.cadastra_paciente(banco_de_dados)
                        break

                    elif op_paciente == 2:
                        paciente.buscar_paciente(banco_de_dados)
                        break

                    elif op_paciente == 3:
                        paciente.listar_paciente(banco_de_dados)
                        break

                    elif op_paciente == 0:
                        print("Saindo Menu Paciente!")
                        break

                    else:
                        print("OPÇÃO INVÁLIDA!")
                except:
                    print("\n-- ERROR! DIGITE APENAS NÚMEROS! ---")


        #Escolha Funcionário
        elif opcao_menu == 2:
            menu.menu_funcionario()
            while (True):
                try:
                    op_funcionario = int(input(">>> "))
                    if op_funcionario == 1:
                        funcionario.cadastrar_funcionario(banco_de_dados)
                        break

                    elif op_funcionario == 2:
                        funcionario.buscar_funcionario(banco_de_dados)
                        break

                    elif op_funcionario == 3:
                        funcionario.listar_funcionario(banco_de_dados)
                        break

                    elif op_funcionario == 0:
                        print("Saindo Menu Funcionário")
                        break

                    else:
                        print("OPÇÃO INVÁLIDA!")
                except:
                    print("\n-- ERROR! DIGITE APENAS NÚMEROS! ---")


        #Escolha Vacina
        elif opcao_menu == 3:
            menu.menu_vacina()
            try:
                while (True):
                    op_vacina = int(input(">>> "))

                    if op_vacina == 1:
                        vacina.registrar_vacina(banco_de_dados)
                        break
                    elif op_vacina == 2:
                        vacina.buscar_vacina(banco_de_dados)
                        break
                    elif op_vacina == 3:
                        vacina.listar_vacina_cpf(banco_de_dados)
                        break
                    elif op_vacina == 4:
                        vacina.listar_registros(banco_de_dados)
                        break
                    elif op_vacina == 0:
                        print("Saindo Menu Vacina")
                        break
                    else:
                        print("OPÇÃO INVÁLIDA!")
            except:
                print("\n-- ERROR! DIGITE APENAS NÚMEROS! ---")


        #Escolha Sair
        elif opcao_menu == 0:
            print("ENCERRANDO APLICATIVO")
            break

        else:
            print("OPÇÃO INVÁLIDA!")

    except:
        print("\n-- ERROR! DIGITE APENAS NÚMEROS! ---")

