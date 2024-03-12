import json

class Vacina():

    def salva_dados(banco_de_dados, dados):
        with open(banco_de_dados) as file:
            json.dump(dados, file, indent=4)

    def registrar_vacina(self, banco_de_dados):
        print("\n--- Registrando Vacina ---")
        nome_pacient = ""
        codigo_vac = input("Informe Códido da Vacina: ")
        tipo_vac = input("[Gripe | Sarampo | COVID] Informe Tipo da Vacina: ")
        cpf = int(input("Informe CPF do paciente: "))

        registro_vac = {"nome": nome_pacient, "codigo": codigo_vac, "tipo": tipo_vac, "cpf": cpf}
        
        try:
            with open(banco_de_dados, 'r') as file:
                dados = json.load(file)

            #Caso o Json exista, mas esteja vazio
            if not dados:
                dados["vacinas"] = [registro_vac]
                self.salva_dados(banco_de_dados, dados)

                print("Vacina {} cadastrada! Paciente {} | CPF: {} !".format(tipo_vac), nome_pacient, cpf)


            else:
                #Caso não esteja vazio, é preciso verificar se já tem vacinas no banco de dados
                if "vacinas" in dados:

                    for d in dados["vacinas"]:
                        if d["codigo"] == codigo_vac:  #É preciso verificar se o código de vacina já foi cadastrado
                            print("Vacina já cadastrada!")
                            break

                    else:
                        for d in dados["vacinas"]:

                            if d["cpf"] == cpf:
                                print("PACIENTE ENCONTRADO... PROSSEGUINDO!")
                                registro_vac["nome"] = d["nome"]
                                dados["vacinas"].append(registro_vac)

                                self.salva_dados(banco_de_dados, dados)
                                print("Vacina aplicada - Paciente: {} | Tipo: {} | Código: {}  ".format(d["nome"], tipo_vac, codigo_vac))
                                break
            
                        else:
                            nome_pacient = input("Nome do Paciente: ")
                            registro_vac["nome"] = nome_pacient
                            dados["vacinas"].append(registro_vac)
                            
                            self.salva_dados(banco_de_dados, dados)
                            print("Vacina Aplicada - Paciente: {} | Tipo: {} | Código: {}  ".format(d["nome"], tipo_vac, codigo_vac))

                else:
                    nome_pacient = input("Nome do Paciente: ")
                    registro_vac["nome"] = nome_pacient
                    dados["vacinas"] = [registro_vac]

                    self.salva_dados(banco_de_dados, dados)
                    print("Vacina Aplicada - Paciente: {} | Tipo: {} | Código: {}  ".format(nome_pacient, tipo_vac, codigo_vac))

        #Caso o arquivo Json não exista
        except FileNotFoundError:
            print("SEM BANCO DE DADOS!")
            print("Aguarde... Estamos Criando.")

            nome_pacient = input("Nome do Paciente: ")
            registro_vac["nome"] = nome_pacient
            novos_dados = {"vacinas": [registro_vac]}

            self.salva_dados(banco_de_dados, novos_dados)
            print("Vacina Aplicada - Paciente: {} | Tipo: {} | Código: {}  ".format(nome_pacient, tipo_vac, codigo_vac))

        #Caso o arquivo Json exista, mas esteja totalmente vazio
        except json.decoder.JSONDecodeError:
            print("SEM BANCO DE DADOS!")
            print("Aguarde... Estamos Criando.")

            nome_pacient = input("Nome do Paciente: ")
            registro_vac["nome"] = nome_pacient
            novos_dados = {"vacinas": [registro_vac]}
            
            self.salva_dados(banco_de_dados, novos_dados)
            print("Vacina Aplicada - Paciente: {} | Tipo: {} | Código: {}  ".format(nome_pacient, tipo_vac, codigo_vac))

