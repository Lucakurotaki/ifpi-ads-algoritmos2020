def main():
    n = int(input("Digite o valor do N: "))
    a = adiciona_itens(n)
    print(verifica_iguais(a))


def adiciona_itens(n):
    lista = []
    for i in range(n):
        lista.append(input("Digite o item: "))

    return lista


def verifica_iguais(v):
    state = "Não existem"

    for i in range(len(v)):
        for j in range(len(v)):
            if i != j and v[i] == v[j]:
                state = "Existem"

    return state + " elementos iguais."


main()
