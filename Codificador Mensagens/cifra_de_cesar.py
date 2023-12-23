##USA A CIFRA DE CÉSAR PARA CODIFICAR MENSAGENS
##A PARTIR DE UMA CHAVE NUMÉRICA ENTRE 1 E 26
import string 

print(
    "_________________________________\n"
    "                                 \n"
    "ATENÇÃO!! NÃO É PERMITIDO NÚMERO \n"
    "                                 \n"
    "_________________________________\n"
    )
chave = int(input("Qual a chave de codificação? Entre 1-26: "))
alfa_original = list(string.ascii_lowercase)
alfa_chave = alfa_original[:chave]
alfa_cifrado = alfa_original[chave:] + alfa_chave

msg_codificada = ''
msg_original = input("Qual mensagem deseja codificar? ").lower().split()
for letra in msg_original:
    for letra2 in list(letra):
        posicao_letra = int(alfa_original.index(letra2))
        codifica_letra = alfa_cifrado[posicao_letra]
        msg_codificada += codifica_letra
    msg_codificada += ' '
    
print(msg_codificada)