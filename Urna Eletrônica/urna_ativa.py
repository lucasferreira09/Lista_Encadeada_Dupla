import funcao_menu
lista_votos = [] #ARMAZENA OS VOTOS REGISTRADOS

def urna_rodando():
    """IRÁ CONTROLAR O FLUXO DA URNA, COMO LOGIN, REGISTROS DE VOTOS, VOTOS INVÁLIDOS"""
    primeiro_voto = 1
    voto_permitido = [1, 2, 3, 4, 0]
    urna_ligada = True
    while urna_ligada:
        funcao_menu.menu_votacao()
        voto_user = int(input("Insira seu voto: "))
        while voto_user not in voto_permitido:
            print("Por Favor. Insira uma das opções acima")
            voto_user = int(input("Insira seu voto: "))               
        if voto_user == 0: 
            if len(lista_votos) == 0: #É PRECISO TER CERTEZA DE QUE O 1° VOTO NÃO É A OPÇÃO 0
                print("\nO primeiro voto deve ser alguma das 4 opções acima")
            else:  #SE NÃO FOR A OPÇÃO 0, ENTÃO JÁ FOI REGISTRADOS VOTOS ANTES
                break  #ASSIM, A URNA É DESLIGADA
        else:
            lista_votos.append(voto_user)
            print("VOTO REGISTRADO COM SUCESSO!!")
    urna_ligada = False
        
def get_votos():
    return lista_votos