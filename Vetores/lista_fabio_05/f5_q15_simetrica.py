def main():
    n = int(input("Digite a ordem do matriz: "))

    matriz = criar_matriz(n)
    simetria = verif_simetria(matriz)

    mostrar_matriz(matriz)

    print("A matriz é " + simetria)


def criar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            num = int(input(f"Digite o {j+1}º número da {i+1}ª linha: "))
            linha.append(num)
        matriz.append(linha)

    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def verif_simetria(matriz):
    simetria = "simétrica"
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                simetria = "assimétrica"

    return simetria


main()
