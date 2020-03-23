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

def dividir_inteiro(x, y):
    if x and y >= 0:
        x = x / y
    return(x)

def dividir(x, y):
    if x and y >= 0:
        x = x // y
    return(x)

def triangulo(x, y, z):
    if x == y and x == z and y == z:
        x = 'triângulo retângulo'
        return(x)

    elif x == y and x == z and y != z:
        x = 'triângulo com 2 lados iguais'
        return(x)

    elif x == y and x != z and y != z:
        x = 'triângulo com apenas 1 lado igual'
        return(x)

    elif x != y and x != z and y != z:
        x = 'triângulo com nenhum lado igual'
        return(x)

    elif x != y and x == z and y != z:
        x = 'triângulo com apenas 1 lado igual'
        return(x)

e = 0

while e != 99:

    e = int(input('Digite 1 para soma ;'
              ' 2 para subtração ;'
              ' 3 para multiplicação ;'
              ' 4 para divisão inteira ; '
              ' 5 para divisão real '
              ' ou 6 para definir um triângulo: '))



    if e == 1:
        h = int(input('Digite um valor para x: '))
        t = int(input('Digite um valor para y: '))
        c = somar(h,t)
        i = int(input('digite 1 para fazer mais uma soma ou 2 para finalizar.'))
        if i == 2:
            print(c)

        elif i == 1:
            n = int(input('Digite um valor para n: '))
            m = int(input('Digite um valor para m: '))
            d = somar(n,m)
            e = c + d
            print(e)

    elif e == 2:
        h = int(input('Digite um valor para x: '))
        t = int(input('Digite um valor para y: '))
        print('valor final:', subtrair(h,t))

    elif e == 3:
        h = int(input('Digite um valor para x: '))
        t = int(input('Digite um valor para y: '))
        print('valor final:', multiplicar(h,t))

    elif e == 4:
        h = int(input('Digite um valor para x: '))
        t = int(input('Digite um valor para y: '))
        print('valor final:', dividir_inteiro(h,t))

    elif e == 5:
        h = int(input('Digite um valor para x: '))
        t = int(input('Digite um valor para y: '))
        print('valor final:', dividir(h,t))

    elif e == 6:
        h = int(input('Digite um valor para x: '))
        t = int(input('Digite um valor para y: '))
        p = int(input('Digite um valor para z: '))
        print('valor final:', triangulo(h,t,p))

