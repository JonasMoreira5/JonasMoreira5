print('********************')
print(' jogo de advinhação  '.upper())
print('********************')
# Mandar o Usuário digitar
num_secreto = 45
total_de_tentativas	=	3
while(total_de_tentativas > 0):
    chut_str = int(input("Digite um número de 1 a 10: "))
    # Variáveis
    acertou = chut_str == num_secreto
    maior = chut_str > num_secreto
    menor = chut_str < num_secreto
    print("Você digitou {}".format(chut_str))
    if (acertou):
        print("Você Acertou!")
        break
    elif (maior):
        print("você errou! Seu chute foi maior que valor a se descobrir.")
    elif (menor):
        print("você errou! Seu chute foi menor que valor a se descobrir.")
    total_de_tentativas = total_de_tentativas - 1
    print("Restam {} tentativas!".format(total_de_tentativas))
    if (total_de_tentativas == 0):
         print("Fim de Jogo!")