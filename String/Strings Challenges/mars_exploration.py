def main():
    s = verifica_s()
    qtd_diferencas = marsExplanation(s)

    print(f"{s} contém {qtd_diferencas} diferenças.")


def marsExplanation(s):
    msg_original = ""
    repeat = len(s) // 3

    for i in range(repeat):
        msg_original += "SOS"

    cont = 0
    for j in range(len(s)):
        if s[j] != msg_original[j]:
            cont += 1

    return cont


def verifica_s():
    state = False

    while state is False:
        s = input("Insira a mensagem recebida na Terra: ")
        if limite_carac(s) and verifica_length(s) and verifica_maiuscula(s):
            state = True
        elif not verifica_length(s):
            print("\nErro. O número de caracteres deve ser múltiplo de 3.\n")
        elif not limite_carac(s):
            print("\nErro. Limite de caracteres excedido.\n")
        elif not verifica_maiuscula(s):
            print("\nErro. A mensagem deve conter somente letras maiúsculas.\n")

    return s


def verifica_length(s):
    return len(s) % 3 == 0


def limite_carac(s):
    return 1 <= len(s) and len(s) <= 99


def verifica_maiuscula(s):
    state = True
    for c in s:
        if diferente_maiuscula(c):
            state = False

    if state is True:
        return True


def diferente_maiuscula(c):
    return ord(c) < 65 or ord(c) > 90


main()
