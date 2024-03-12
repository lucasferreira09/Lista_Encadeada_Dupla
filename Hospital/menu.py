class Menu():
    """APENAS MOSTRA OS MENUS!"""
    
    def menuInicial(self):
        print("\n=========== MENU INICIAL ==========\n")
        print("1. Paciente")
        print("2. Funcionário")
        print("3. Vacina")
        print("0. SAIR")

    def menu_paciente(self):
        print("\n=========== MENU PACIENTE ==========\n")
        print("1. Cadastrar")
        print("2. Buscar por CPF")
        print("3. Listar todos")
        print("0. SAIR")

    def menu_funcionario(self):
        print("\n======== MENU FUNCIONÁRIO ========\n")
        print("1. Cadastrar")
        print("2. Buscar por CPF")
        print("3. Listar todos")
        print("0. SAIR")
        
    def menu_vacina(self):
        print("\n=========== MENU VACINA ===========\n")
        print("1. Registrar vacinação")
        print("2. Buscar Vacina por Código")
        print("3. Listar vacinas por CPF do Paciente")
        print("4. Listar todos os registros")
        print("0. SAIR")
            