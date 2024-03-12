import json    

class Funcionario():

    def cadastrar_funcionario(self, banco_dados, dados_cadastrado):
        print("\n--- Cadastrando Funcionário ---")
        funcionario = {}
        nome = input("Informe o nome do Funcionário: ").title()
        cpf = int(input("[Somente números] Informe o CPF do Funcionário: "))
        
        funcionario["nome"] = nome
        funcionario["cpf"] = cpf

        try:
            with open(banco_dados, 'r') as file:
                dados = json.load(file)

            if not dados:
                dados["funcionarios"] = [funcionario]
                with open(banco_dados, 'w') as file:
                    json.dump(dados, file, indent=4)
                    print("Funcionário {} Cadastrado com Sucesso!".format(nome).title())

            else:  #Caso não esteja vazio, é preciso verificar se já tem Funcionários no banco de dados
                if "funcionarios" in dados:
                    for d in dados["funcionarios"]:
                        if d["cpf"] == cpf:
                            print("Funcionário {} já Cadastrado!".format(nome).title())
                            break

                    else:  #Se não tiver, adicionamos
                        dados["funcionarios"].append(funcionario)
                        with open(banco_dados, 'w') as file:
                            json.dump(dados, file, indent=4)
                            print("Funcionário {} Cadastrado com Sucesso!".format(nome).title())
                    
                else:  #Caso não tenha nem um Funcionários no banco de dados, criamos um
                    dados["funcionarios"] = [funcionario]
                    with open(banco_dados, 'w') as file:
                        json.dump(dados, file, indent=4)
                        print("Funcionário {} Cadastrado com Sucesso!".format(nome).title())
                
        
        #Caso o arquivo Json não exista
        except FileNotFoundError:
            print("SEM BANCO DE DADOS!")
            print("Aguarde... Estamos Criando.")

            with open(banco_dados, 'w') as file:
                dados_cadastrado["funcionarios"] = [funcionario]
                json.dump(dados_cadastrado, file, indent=4)
                print("Paciente {} Cadastrado com Sucesso".format(nome).title())
        

        #Caso o arquivo Json exista, mas esteja totalmente vazio
        except json.decoder.JSONDecodeError:
            print("SEM BANCO DE DADOS!")
            print("Aguarde... Estamos Criando.")

            novos_dados = {"funcionarios": [funcionario]}
            with open(banco_dados, 'w') as file:
                json.dump(novos_dados, file, indent=4)
                print("Funcionário {} Cadastrado com Sucesso".format(nome).title())



    def buscar_funcionario(self, banco_dados):
        print("\n--- Buscando Funcionário ---")
        
        busca_cpf = int(input("Insira o CPF do Funcionário: "))
        try:
            with open(banco_dados, 'r') as file:
                dados = json.load(file)

            if not dados:
                print("NÃO HÁ PACIENTES CADASTRADOS")

            else:
                if "funcionarios" in dados:  #Verifica se há algum Funcionário no banco de dados
                    for d in dados["funcionarios"]:
                        if d["cpf"] == busca_cpf:
                            print("O Funcionário {} com CPF {}, está cadastrado.".format(d["nome"], busca_cpf))
                            break
                    else:
                        print("FUNCIONÁRIO NÃO ENCONTRADO")
                            
        #Caso o arquivo Json não exista
        except FileNotFoundError:
                print("SEM BANCO DE DADOS!")
        
        #Caso o arquivo Json exista, mas esteja totalmente vazio
        except json.decoder.JSONDecodeError:
            print("SEM BANCO DE DADOS!")


    def listar_funcionario(self, banco_dados):
        print("\n--- Listando Funcionário ---")
        
        try:
            with open(banco_dados, 'r') as file:
                dados = json.load(file)

            if not dados:
                print("NÃO HÁ FUNCIONÁRIOS CADASTRADOS")

            else:
                if "funcionarios" in dados:  #Verifica se há algum Funcionário no banco de dados
                    n = 1
                    for d in dados["funcionarios"]:
                        print("{}). Funcionário: {} | CPF: {} ".format(n, d["nome"], d["cpf"] ))
                        n += 1
                else:
                    print("NÃO HÁ FUNCIONÁRIOS CADASTRADOS")
                            
        #Caso o arquivo Json não exista
        except FileNotFoundError:
            print("SEM BANCO DE DADOS!")
        
        #Caso o arquivo Json exista, mas esteja totalmente vazio
        except json.decoder.JSONDecodeError:
            print("SEM BANCO DE DADOS!")
        
