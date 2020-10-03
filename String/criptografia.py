def main():
    n = num_positivo("Digite o número de linhas: ")

    mensagem_codificada = criptografia(n)

    print(mensagem_codificada)


def criptografia(n):
    if verif_n(n):
        mensagem_cript = ""
        for i in range(n):
            msg = input("Digite a mensagem: ")
            if verif_m(len(msg)):
                mensagem_cript += "\n"
                mensagem_cript += codifica(msg)
    return mensagem_cript


def verif_n(n):
    return n >= 1 and n <= 1*10**4


def verif_m(m):
    return m >= 1 and m <= 1*10**3


def codifica(msg):
    texto_rotacionado = ""
    for c in msg:
        if verif_letra(c):
            texto_rotacionado += rotac_carac(c)
        else:
            texto_rotacionado += c

    texto_inverso = inverte(texto_rotacionado)

    texto_codificado = ""
    metade_texto = len(texto_inverso)//2

    for i in range(metade_texto):
        texto_codificado += texto_inverso[i]

    for j in range(metade_texto, len(msg)):
        texto_codificado += desloca(texto_inverso[j])

    return texto_codificado


def letra_maiuscula(carac):
    return ord(carac) >= 65 and ord(carac) <= 90


def letra_minuscula(carac):
    return ord(carac) >= 97 and ord(carac) <= 122


def verif_letra(carac):
    return letra_maiuscula(carac) or letra_minuscula(carac)


def rotac_carac(c):
    cod = ord(c)
    cod_novo = cod + 3

    carac_novo = chr(cod_novo)
    return carac_novo


def inverte(msg):
    msg_inverso = ""
    for i in range(len(msg)-1, -1, -1):
        msg_inverso += msg[i]

    return msg_inverso


def desloca(c):
    cod = ord(c)
    cod_novo = chr(cod - 1)

    return cod_novo


def num_positivo(mssg):
    num = int(input(mssg))

    while num < 1:
        num = int(input('Erro! ' + mssg))

    return num


main()
