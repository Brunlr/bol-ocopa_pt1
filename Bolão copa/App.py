def ciano(txt):
    print (f'\033[1;36m{txt}\033[m')


def azul(txt):
    print (f'\033[1;34m{txt}\033[m')


def verde(txt):
    print (f'\033[0;32m{txt}\033[m')



def vermelho(txt):
    print(f'\033[1;31m{txt}\033[m')




print (f'\033[1;34m')
print("_"*30)
print("BOLÃO DA COPA".center(30))
print("_"*30)

times = ('Croacia', 'Brasil')
cont = 0        #contador
li = list()      #lista principal
nl = list()      #lista que adiciona lista
cond = 0  #condicional
while True:
    print(f'\033[1;34m')
    nl.clear()
    # Estrutura de validação Nome
    nl.append(str(input('Digite o nome: ').strip().lower()).capitalize())

    if li!=[]:     #a lista entra na condicional apenas se tiver elementos
        a = 1
        while a!=0:                    #apenas quando o 'a' passa a valer 0, a repetição é encerrada
            for e in li:
                if e[0] == nl[0]:
                    vermelho(f'O usuário {e[0]} já possui palpite, não é possivel 2 palpites!')
                    print(f'\033[1;34m')
                    while True:

                        nl[0] = str(input('Digite seu nome: '))
                        if e[0] != nl[0]:
                            break
                        else:

                            vermelho('ERRO! Nome ja ultilizado!')
                            print(f'\033[1;34m')
                            continue
                else:
                    a = 0
    # Estrutura de palpite
    nl.append(int(input(f'Usuario {nl[0]}, Digite o número de gols do time {times[0]}: ')))
    nl.append(int(input(f'Usuario {nl[0]}, Digite o numero de gols do time {times[1]}: ')))
    e = 0     #o elemento 'e' é zerado novamente para não ocorrer interferências
    if len(li)>0:         #apenas entrará na condicional se o tiver mais de uma lista na lista principal
        while a != 1:        #apenas quando o 'a' passa a valer 1, a repetição é encerrada
            for e in li:
                if e[1] == nl[1]:
                    if e[2]== nl[2]:
                        vermelho(f'O usuário {e[0]} já fez o palpite de {nl[1]}x{nl[2]}, não é possivel 2 palpites iguais!')
                        print(f'\033[1;34m')
                        while True:
                            nl[1] = int(input(f'Usuario {nl[0]}, Digite o número de gols do time {times[0]}: '))
                            nl[2] = int(input(f'Usuario {nl[0]}, Digite o numero de gols do time {times[1]}: '))
                            if nl[1] and nl[2] != e[1] and e[2]:
                                break
                            else:
                                vermelho('ERRO! Palpite ja ultilizado!')
                                print(f'\033[1;34m')
                                continue
                else:
                    a = 1
    print(f'\033[m\033[1;36m')

    li.append(nl[:])
    while True:    #loop para condicional
        cond = int(input('1 - Adicionar novo usuário\n2 - Encerrar\nDigite sua opção: '))
        if cond == 1 or cond == 2:
            if cond == 2:
                vermelho('Você optou por encerrar o programa')
            break
    if cond == 2:
        break
    print('\033[m')


print (f'\033[0;32m')
print('{:<12} {:<10} {:<10}'.format('Usuario', times[0] ,times[1] ))
for c in li:
    for d in c:
        if d == c[0]:
            print(f"\033[33m{d:<10}\033[m", end='\033[0;32m|  \033[m')
        elif d == c[1]:
            print(f"\033[33m{d:<8}\033[m", end='\033[0;32m|  \033[m')
        else:
            print(f"\033[33m{d:<8}\033[m", end='\033[0;32m|  \033[m')

    print()

