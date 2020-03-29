def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mA OPÇÃO É INVALIDA, INSIRA UM VALOR VALIDO.\033[m')
            continue
        except KeyboardInterrupt:
            print('O USUARIO PREFERIU INTERROMPER O PROGRAMA')
            return 0
        else:
            return n

def linha(tam=40):
    print('-'*tam)


def cabecalho(txt):
    linha()
    print(txt.center(30))
    linha()

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    opc = leiaInt('Sua opção: ')
    return opc
