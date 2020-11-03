def main():
    n = int(input("Digite a ordem do matriz: "))

    matriz = criar_matriz(n)

    soma_prin = somar_prin(matriz)
    soma_sec = somar_sec(matriz)
    soma_res = somar_res(matriz)

    print(f"Soma da diagonal principal: {soma_prin}\n"
          f"Soma da diagonal secundária: {soma_sec}\n"
          f"Soma dos outros números: {soma_res}")


def criar_matriz(n):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            num = int(input(f"Insira o {j+1}º número da {i+1}ª linha: "))
            linha.append(num)
        matriz.append(linha)

    return matriz


def somar_sec(matriz):
    soma = 0
    cont = len(matriz)-1
    for i in range(len(matriz)):
        soma += matriz[i][cont]
        cont -= 1

    return soma


def somar_prin(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]

    return soma


def somar_res(matriz):
    soma = 0
    cont = len(matriz)-1
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j != i and j != cont:
                soma += matriz[i][j]
        cont -= 1

    return soma


main()
