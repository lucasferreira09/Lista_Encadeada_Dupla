import json

class Paciente():

    def salva_dados(self, banco_de_dados, dados):
        with open(banco_de_dados, 'w') as file:
            json.dump(dados, file, indent=4)

    
    def cadastra_paciente(self, banco_de_dados):
        print("--- Cadastrando Paciente ---")

        nome = input("Informe o nome do paciente: ")
        cpf = int(input("[Somente números] Informe o CPF do paciente: "))
        contato = input("Informe algo para contato. [E-mail ou Telefone]: ")

        paciente = {"nome":nome, "cpf": cpf, "contato":contato}
        
        try:
            with open(banco_de_dados, 'r') as file:
                dados = json.load(file)

            #Caso o Json exista, mas esteja vazio
            if not dados:
                dados["pacientes"] = [paciente]
                
                self.salva_dados(banco_de_dados, dados)
                print("Paciente {} Cadastrado com Sucesso!".format(nome).title())

            else:
                #Caso não esteja vazio, é preciso verificar se já tem pacientes no banco de dados
                if "pacientes" in dados:

                    for d in dados["pacientes"]: #É preciso verificar se o paciente já está cadastrado
                        if d["cpf"] == cpf:
                            print("Paciente {} já Cadastrado!".format(nome).title())
                            break
                    
                    else:  #Se não tiver, adicionamos
                        dados["pacientes"].append(paciente)

                        self.salva_dados(banco_de_dados, dados)
                        print("Paciente {} Cadastrado com Sucesso!".format(nome).title())
               
                else:#Caso não tenha nem um paciente no banco de dados, criamos um
                    dados["pacientes"] = [paciente]
                    self.salva_dados(banco_de_dados, dados)
                    
                    print("Paciente {} Cadastrado com Sucesso!".format(nome).title())
                
        
        #Caso o arquivo Json não exista
        except FileNotFoundError:
            print("SEM BANCO DE DADOS!")
            print("Aguarde... Estamos Criando.")

            novos_dados = {"pacientes": [paciente]}
            self.salva_dados(banco_de_dados, novos_dados)

            print("Paciente {} Cadastrado com Sucesso".format(nome).title())
        
        #Caso o arquivo Json exista, mas esteja totalmente vazio
        except json.decoder.JSONDecodeError:
            print("SEM BANCO DE DADOS!")
            print("Aguarde... Estamos Criando.")

            novos_dados = {"pacientes": [paciente]}
            self.salva_dados(banco_de_dados, novos_dados)
            
            print("Paciente {} Cadastrado com Sucesso".format(nome).title())


    def buscar_paciente(self, banco_de_dados):
        print("\n--- Buscando Paciente ---")

        busca_cpf = int(input("Insira o CPF do Paciente: "))
        try:
            with open(banco_de_dados, 'r') as file:
                dados = json.load(file)

            if not dados:
                print("NÃO HÁ PACIENTES CADASTRADOS")
                
            else:
                if "pacientes" in dados:  #Verifica se há algum paciente no banco de dados
                    for d in dados["pacientes"]:
                        if d["cpf"] == busca_cpf:
                            print("O Paciente {} com CPF {}, está cadastrado.".format(d["nome"], busca_cpf))
                            break
                    else:
                        print("PACIENTE NÃO ENCONTRADO")
                            
        #Caso o arquivo Json não exista
        except FileNotFoundError:
            print("SEM BANCO DE DADOS!")
        
        #Caso o arquivo Json exista, mas esteja totalmente vazio
        except json.decoder.JSONDecodeError:
            print("SEM BANCO DE DADOS!")


    def listar_paciente(self, banco_de_dados):
        print("\n--- Listando Paciente ---")

        try:
            with open(banco_de_dados, 'r') as file:
                dados = json.load(file)
                
                if not dados:
                    print("NÃO HÁ PACIENTES CADASTRADOS")

                else:
                    if "pacientes" in dados:  #Verifica se há algum paciente no banco de dados
                        n = 1
                        for d in dados["pacientes"]:
                            print("{}) Paciente: {} | CPF: {} ".format(n, d["nome"], d["cpf"] ))
                            n += 1
                    else:
                        print("NÃO HÁ PACIENTES CADASTRADOS")
                            
        #Caso o arquivo Json não exista
        except FileNotFoundError:
            print("SEM BANCO DE DADOS!")
        
        #Caso o arquivo Json exista, mas esteja totalmente vazio
        except json.decoder.JSONDecodeError:
            print("SEM BANCO DE DADOS!")
        
