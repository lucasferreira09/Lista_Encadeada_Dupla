import statistics
import urna_ativa
import funcao_calcula
import funcao_menu

urna_ativa.urna_rodando()
funcao_calcula.calcula_votos(urna_ativa.get_votos())

from statistics import mode
empate = statistics.multimode(urna_ativa.get_votos())
if len(empate) > 1:
    print("\nTEMOS UM EMPATE! ")
else:    
    vencedor = statistics.mode(urna_ativa.get_votos())
    if vencedor == 1:
        print("\nA VENCEDORA É MARIA")
    elif vencedor == 2:
        print("\nO VENCEDOR É JOÃO")
    elif vencedor == 3:
        print("\nO VENCEDOR É PEDRO")