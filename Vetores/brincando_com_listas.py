def main():

    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor (posição)'
    menu += '\n 3 - Mostrar Valor (todos)'
    menu += '\n 4 - Remover Valor (posição)'
    menu += '\n 5 - Atualizar Valor (posição)'
    menu += '\n 6 - Contagens (geral)'
    menu += '\n 7 - Mostrar Média'
    menu += '\n 8 - Dobrar Valores (todos)'
    menu += '\n 9 - Dobrar Multiplos'
    menu += '\n 10 - Apagar todos os valores'
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> '

    lista = []

    while True:  # Condição sempre verdadeira, só irá para em caso..
        # ..de break ou error
        opcao = int(input(menu))

        # Verificar operacao a fazer de acordo com a opcao
        if opcao == 1:
            # Listas quando passadas como argumentos e modificadas por
            # funções não é necessário retorná-las
            # Se modificar a lista dentro de um função, as variáveis que já
            # apontavam para ela terão acesso a lista moficiada normalmente
            # Por isso nao está ```lista = inserir_valores(lista)````
            inserir_valores(lista)
        elif opcao == 2:
            mostra_valor(lista)
        elif opcao == 3:
            mostrar_todos(lista)
        elif opcao == 4:
            remover_valor(lista)
        elif opcao == 5:
            atualizar_valor(lista)
        elif opcao == 6:
            contagens_geral(lista)
        elif opcao == 7:
            mostrar_media(lista)
        elif opcao == 8:
            dobrar_valores(lista)
        elif opcao == 9:
            dobrar_multiplos(lista)
        elif opcao == 10:
            apagar_tudo(lista)
        elif opcao == 0:  # sair do while
            break
        else:
            print('Opção Inválida')

        input('<enter> to continue...')


def inserir_valores(lista):
    qtd = int(input('Quantos valores desejar inserir?'))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')


def mostra_valor(lista):
    posicao = int(input('Qual posição? '))
    print('Valor buscado:')
    print(f'Valor index[{posicao}] é {lista[posicao]}')


def mostrar_todos(colecao):
    tamanho = len(colecao)
    print(f'**** Mostrando {tamanho} valores ****')
    for valor in colecao:
        print(f'>> {valor}')


def remover_valor(valores):
    posicao = int(input('Qual posição vc quer remover? '))

    removido = valores.pop(posicao)
    print(f'O valor {removido} foi removido da posição {posicao}!')


def atualizar_valor(cesta):
    pos = int(input('Qual posição? '))

    valor = cesta[pos]
    print(f'Na posição {pos} existe atualmente o valor {valor}')

    novo_valor = int(input('Qual o novo valor? '))
    cesta[pos] = novo_valor
    print('Valor atualizado com sucesso!')


def contagens_geral(lista):
    print("**** Mostrando Contagens ****")
    print(f"\nPares: {pares(lista)}\nÍmpares: {impares(lista)}"
          f"\nNegativos: {negativos(lista)}\nPositivos: {positivos(lista)}"
          f"\nPrimos: {primos(lista)}\nZerados: {zerados(lista)}")


def mostrar_media(lista):
    print("**** Mostrando a média ****")
    print(media(lista))


def dobrar_valores(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]*2

    print(lista)

    print("Todos os valores dobrados com sucesso!")


def dobrar_multiplos(lista):
    num = int(input("Multiplos de qual número deseja dobrar?"))

    for i in range(len(lista)):
        if lista[i] % num == 0:
            lista[i] = lista[i]*2

    print(lista)
    print(f"Todos os múltiplos de {num} dobrados com sucesso!")


def pares(lista):
    cont = 0
    for i in lista:
        if i % 2 == 0:
            cont += 1

    return cont


def impares(lista):
    cont = 0
    for i in lista:
        if i % 2 != 0:
            cont += 1

    return cont


def negativos(lista):
    cont = 0
    for i in lista:
        if i < 0:
            cont += 1

    return cont


def positivos(lista):
    cont = 0
    for i in lista:
        if i >= 0:
            cont += 1

    return cont


def primos(lista):
    cont = 0
    for i in lista:
        if i in [1, 2, 3, 5, 7]:
            cont += 1
        elif (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0):
            cont += 1

    return cont


def zerados(lista):
    cont = 0
    for i in lista:
        if i == 0:
            cont += 1

    return cont


def media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    media = soma/len(lista)

    return media


def apagar_tudo(lista):
    for i in range(len(lista)):
        del lista[0]
    print("Todos os valores apagados com sucesso!")


main()
