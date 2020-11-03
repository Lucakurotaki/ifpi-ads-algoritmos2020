def main():

    n = lista_binario()

    b = binario(n)

    h = hexadecimal(n)

    d = decimal(n)

    print(f"{b} binário = {h} hexadecimal = {d} decimal")


def lista_binario():
    lista = []

    for i in range(8):
        lista.append(e_bin(i))

    return lista


def e_bin(i):
    state = False
    while state is False:
        num = int(input(f"Digite o {i+1}º número: "))
        if num == 0 or num == 1:
            state = True
            return num


def binario(n):
    lista = n
    num = ""

    for i in range(len(lista)):
        num += str(lista[i])

    return num


def decimal(n):
    lista = n

    n_dec = conversao(lista)

    return n_dec


def conversao(n):
    lista = n

    cont = len(lista)-1
    num = 0

    for i in range(len(lista)):
        num += lista[i]*2**cont
        cont -= 1

    return num


def hexadecimal(n):
    lista_bin = n

    lista1 = []
    lista2 = []

    for i in range(len(lista_bin)):
        if i <= 3:
            lista1.append(lista_bin[i])
        else:
            lista2.append(lista_bin[i])

    num1 = conversao(lista1)
    num2 = conversao(lista2)

    num1 = e_letra(num1)
    num2 = e_letra(num2)

    n_hex = str(num1) + str(num2)

    return n_hex


def e_letra(n):
    num = n
    if num > 9:
        num = chr(65+(num-10))

    return num


main()
