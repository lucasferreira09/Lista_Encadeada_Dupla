import statistics
import urna_ativa

def calcula_votos(votos):
    """IRÁ CALCULAR O NÚMERO DE VOTOS E AS RESPECTIVAS PORCENTAGENS"""

    voto_maria = votos.count(1)
    voto_joao = votos.count(2)
    voto_pedro = votos.count(3)
    voto_anulado = votos.count(4)

    #DIVIDE OS VOTOS DE CADA CANDIDATO PELA QUANTIDADE TOTAL E TRANSFORMA EM %
    percentual_voto = [voto_maria/len(votos), voto_joao/len(votos), voto_pedro/len(votos), voto_anulado/len(votos)]
    
    from statistics import mode
    max_votos = statistics.mode(urna_ativa.get_votos())
    if max_votos == 4:
        print("\nEleição Cancelada! ")
        print("SEM VOTOS SUFICIENTES!")
    else:
        print("\n%d Votos para Maria, com %.2f%% dos votos" %(voto_maria, percentual_voto[0]*100))
        print("%d Votos para João, com %.2f%% dos votos" %(voto_joao, percentual_voto[1]*100))
        print("%d Votos para Pedro, com %.2f%% dos votos" %(voto_pedro, percentual_voto[2]*100))
        print("%d Votos Anulados, com %.2f%% dos votos" %(voto_anulado, percentual_voto[3]*100))
    return percentual_voto
