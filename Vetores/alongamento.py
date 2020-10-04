def main():
    n = int(input("Quantos números pretende digitar?: "))

    vetor = criar_vetor(n)

    print("\nNa lista original:", apresentar_contagens(vetor))

    vetor = substituir(vetor)

    print("\nNa lista modificada:", apresentar_contagens(vetor))

    print("\nA média de valores é: ", media(vetor))


def criar_vetor(n):
    v = [-1] * n
    for i in range(len(v)):
        v[i] = int(input(f"Digite o {i+1}º número: "))

    return v


def apresentar_contagens(v):
    return f"\nPares: {pares(v)}\nÍmpares: {impares(v)}\nNegativos: {negativos(v)}\nPositivos: {positivos(v)}"


def pares(v):
    cont = 0
    for i in v:
        if i % 2 == 0:
            cont += 1

    return cont


def impares(v):
    cont = 0
    for i in v:
        if i % 2 != 0:
            cont += 1

    return cont


def negativos(v):
    cont = 0
    for i in v:
        if i < 0:
            cont += 1

    return cont


def positivos(v):
    cont = 0
    for i in v:
        if i >= 0:
            cont += 1

    return cont


def substituir(v):
    vetor_novo = v
    for i in range(len(v)):
        if i >= 0:
            vetor_novo[i] = vetor_novo[i]*2
        else:
            vetor_novo[i] = vetor_novo[i]/2

    return vetor_novo


def media(v):
    soma = 0
    for i in range(len(v)):
        soma += v[i]
    media = soma/len(v)

    return media


main()
