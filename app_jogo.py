from os import system
from random import randint
from time import sleep

lista_objetos = ['✊','🖐️','✌️','🫳','🖖']
numeros_permitidos = ['0','1','2','3','4']

system('cls')

print('Vamos jogar pedra-papel-tesoura-lagarto-spock')

def msg_inicio():
    print('Selecione um número abaixo para escolher sua ação')
    pos = 0
    for mao in lista_objetos:
        print(pos, mao)
        pos+=1

msg_inicio()
jogador = input('\nDigite sua escolha: ')

while jogador not in numeros_permitidos:
    system('cls')
    print('Opção inválida!')
    msg_inicio()
    jogador = input('\nDigite sua escolha: ')
 
jogador = int(jogador)    
computador = randint(0,4)

acao_jogador = lista_objetos[jogador]
acao_computador = lista_objetos[computador]

sleep(2)
system('cls')
print(f'''         COMBATE!
    JOGADOR VS COMPUTADOR
      {acao_jogador}           {acao_computador}   ''')


if jogador == computador:
    print('        >> EMPATE <<')
elif (acao_jogador == "✊" and acao_computador == "✌️") or \
     (acao_jogador == "✌️" and acao_computador == "🖐️") or \
     (acao_jogador == "🖐️" and acao_computador == "✊") or \
     (acao_jogador == "✊" and acao_computador == "🫳") or \
     (acao_jogador == "🫳" and acao_computador == "🖖") or \
     (acao_jogador == "🖖" and acao_computador == "✌️") or \
     (acao_jogador == "✌️" and acao_computador == "🫳") or \
     (acao_jogador == "🫳" and acao_computador == "🖐️") or \
     (acao_jogador == "🖐️" and acao_computador == "🖖") or \
     (acao_jogador == "🖖" and acao_computador == "✊"):
        print('        >> VITÓRIA <<')
else:
    print('        >> DERROTA <<')
    sleep(0.5)
    print('Jogue novamente para tentar vencer')