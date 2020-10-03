def main():
    s = verifica_s()
    qtd_palavras = camelcase(s)

    print(f"{s} contém {qtd_palavras} palavras.")


def camelcase(s):
    num = 1
    for c in s:
        if letra_maiuscula(c):
            num += 1

    return num


def letra_maiuscula(letra):
    return ord(letra) >= 65 and ord(letra) <= 90


def verifica_s():
    state = False
    while state is False:
        s = input("Escreva a sequência de palavras em Camel Case: ")
        if limite_carac(s) and verifica_espaco(s):
            state = True
        elif not verifica_espaco(s):
            print("\nErro. A frase não deve conter espaços.\n")
        elif not limite_carac(s):
            print("\nErro. Limite de caracteres excedido.")

    return s


def limite_carac(s):
    qtd_carac = len(s)
    return 1 <= qtd_carac and qtd_carac <= 10**5


def verifica_espaco(s):
    return " " not in s


main()
