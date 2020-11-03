def main():
    n = int(input("Digite a quantidade de items do vetor: "))

    lista = criar_lista(n)

    maior = maior_item(lista)
    menor = menor_item(lista)

    maj_pos = posicao(maior, lista)
    min_pos = posicao(menor, lista)

    print(f"Maior item: {maior}, posição {maj_pos}"
          f"\nMenor item: {menor}, posição {min_pos}")


def criar_lista(n):
    lista = []
    for i in range(n):
        num = int(input(f"Digite o {i+1}º item: "))
        lista.append(num)

    return lista


def maior_item(lista):
    maior = lista[0]
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[j] > maior:
                maior = lista[j]

    return maior


def menor_item(lista):
    menor = lista[0]
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[j] < menor:
                menor = lista[j]

    return menor


def posicao(num, lista):
    for i in range(len(lista)):
        if lista[i] == num:
            return i


main()
