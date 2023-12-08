import funcao_menu
lista_votos = [] #ARMAZENA OS VOTOS REGISTRADOS

def urna_rodando():
    """IRÁ CONTROLAR O FLUXO DA URNA, COMO LOGIN, REGISTROS DE VOTOS, VOTOS INVÁLIDOS"""
    primeiro_voto = 1
    voto_permitido = [1, 2, 3, 4, 0]
    urna_ligada = True

    while urna_ligada:
        funcao_menu.menu_votacao()
        ##SÓ PERMITE UM VALOR INTEIRO
        try:
            voto_user = int(input("Insira seu voto: "))
        except ValueError:
            ##SE NÃO FOR INTEIRO VOLTA PARA O INÍCIO
            print("INSIRA UM INTEIRO")
            continue

        while voto_user not in voto_permitido: ##GARANTE QUE SOMENTE VOTOS PERMITIDOS SEJAM REGISTRADOS
            print("Por Favor. Insira uma das opções acima")
            voto_user = int(input("Insira seu voto: "))               
        if voto_user == 0: 
            if len(lista_votos) == 0: #É PRECISO TER CERTEZA DE QUE O 1° VOTO NÃO É A OPÇÃO 0
                print("\nO primeiro voto deve ser alguma das 4 opções acima")
            else:  #SE NÃO FOR A OPÇÃO 0, ENTÃO JÁ FOI REGISTRADOS VOTOS ANTES
                urna_ligada = False  #ASSIM, A URNA É DESLIGADA
        else:
            lista_votos.append(voto_user) ##COMO O VOTO NÃO É 0, ELE É ARMAZENADO NA LISTA
            print("VOTO REGISTRADO COM SUCESSO!!")
    
        
def get_votos():
    return lista_votos