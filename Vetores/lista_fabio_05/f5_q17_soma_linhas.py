def main():
    n = int(input("Digite a ordem da matriz: "))

    matriz = criar_matriz(n)

    mostrar_matriz(matriz)

    maj = maior(matriz)
    min = menor(matriz)

    print(f"A linha com maior soma: {maj}ª linha\n"
          f"A linha com menor soma: {min}ª linha")


def criar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            num = int(input(f"Insira o {j+1}º número da {i+1}ª linha: "))
            linha.append(num)
        matriz.append(linha)

    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def maior(matriz):
    maior_linha = 1
    maior_soma = 0

    for i in range(len(matriz)):
        maior_soma += matriz[0][i]

    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz)):
            soma += matriz[i][j]
        if soma > maior_soma:
            maior_soma = soma
            maior_linha = i+1

    return maior_linha


def menor(matriz):
    menor_linha = 1
    menor_soma = 0

    for i in range(len(matriz)):
        menor_soma += matriz[0][i]

    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz)):
            soma += matriz[i][j]
        if soma < menor_soma:
            menor_soma = soma
            menor_linha = i + 1

    return menor_linha


main()
