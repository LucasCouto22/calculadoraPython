def somar(x, y):
    if x and y >= 0:
        x = x + y
    return(x)

def subtrair(x, y):
    if x and y >= 0:
        x = x - y
    return(x)

def multiplicar(x, y):
    if x and y >= 0:
        x = x * y
    return(x)

def dividirInteiro(x, y):
    if x and y >= 0:
        x = x / y
    return(x)

def dividir(x, y):
    if x and y >= 0:
        x = x // y
    return(x)

def porcentagem(x, y):
    if x and y >= 0:
        x = x * y
        x = x / 100
        return(x)

def exponencial(x, y):
    if x and y >= 0:
        x = x ** y
        return(x)

def raizQuadrada(x):
    if x >= 0:
        x = x ** 0.5
        return(x)


controller = 0
fim = 0

while controller != 2:




    if controller == 1 or controller == 0:
        e = int(input('Digite um número para escolher: \n'
                  ' 1 para soma \n'
                  ' 2 para subtração \n'
                  ' 3 para multiplicação \n'
                  ' 4 para divisão inteira  \n'
                  ' 5 para divisão real \n '
                  '6 para porcentagem \n'
                  ' 7 para exponencial \n'
                  ' 8 para raiz quadrada: '))

        if e == 1:
            if controller == 0:
                h = int(input('Digite um valor: '))
                t = int(input('Digite um valor para somar: '))
                c = somar(h, t)
                fim = c
                print('Resultado: ', fim)


            elif controller == 1:
                t = int(input('Digite um valor para somar: '))
                c = somar(fim, t)
                fim = c
                print('Resultado: ', fim)



        elif e == 2:
            if controller == 0:
                h = int(input('Digite um valor: '))
                t = int(input('Digite um valor para subtrair: '))
                c = subtrair(h, t)
                fim = c
                print('Resultado: ', fim)


            elif controller == 1:
                t = int(input('Digite um valor para subtrair: '))
                c = subtrair(fim, t)
                fim = c
                print('Resultado: ', fim)

        elif e == 3:
            if controller == 0:
                h = int(input('Digite o primeiro valor: '))
                t = int(input('Digite o segundo valor: '))
                c = multiplicar(h, t)
                fim = c
                print('Resultado: ', fim)


            elif controller == 1:
                t = int(input('Digite um valor para multiplicar: '))
                c = multiplicar(fim, t)
                fim = c
                print('Resultado: ', fim)


        elif e == 4:
            if controller == 0:
                h = int(input('Digite o valor a ser dividido: '))
                t = int(input('Digite o valor divisor: '))
                c = dividirInteiro(h, t)
                fim = c
                print('Resultado: ', fim)


            elif controller == 1:
                t = int(input('Digite um valor para divisor: '))
                c = dividirInteiro(fim, t)
                fim = c
                print('Resultado: ', fim)

        elif e == 5:
            if controller == 0:
                h = int(input('Digite o valor a ser dividido: '))
                t = int(input('Digite o valor divisor: '))
                c = dividir(h, t)
                fim = c
                print('Resultado: ', fim)


            elif controller == 1:
                t = int(input('Digite um valor para divisor: '))
                c = dividir(fim, t)
                fim = c
                print('Resultado: ', fim)

        elif e == 6:
            if controller == 0:
                h = int(input('Digite o valor: '))
                t = int(input('Digite a porcentagem: '))
                c = porcentagem(h, t)
                fim = c
                print('Resultado final: ', fim,'%')
                break;


            elif controller == 1:
                t = int(input('Digite o valor para descobrir porcentagem: '))
                c = porcentagem(fim, t)
                fim = c
                print('Resultado final: ', fim,'%')
                break;

        elif e == 7:
            if controller == 0:
                h = int(input('Digite o valor: '))
                t = int(input('Elevado a: '))
                c = exponencial(h, t)
                fim = c
                print('Resultado: ', fim)


            elif controller == 1:
                t = int(input('Elevado a: '))
                c = exponencial(fim, t)
                fim = c
                print('Resultado: ', fim)

        elif e == 8:
            if controller == 0:
                t = int(input('Número para descobrir raiz quadrada: '))
                c = raizQuadrada(t)
                fim = c
                print('Resultado: ', fim)

            elif controller == 1:
                c = raizQuadrada(fim)
                fim = c
                print('Resultado: ', fim)




    controller = int(input('Deseja continuar? \n'
                           'Se sim digite 1, se não digite 2: '))
    if controller == 2:
        print('Valor Final: ',fim)
        break;

