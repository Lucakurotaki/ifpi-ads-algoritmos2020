def main():
    print("\n~~~Primeira data~~~")
    ano1 = int(input("Digite o ano: "))
    mes1 = int(input("Digite o mês: "))
    dia1 = int(input("Digite o dia: "))

    print("\n~~~Segunda data~~~")
    ano2 = int(input("Digite o ano: "))
    mes2 = int(input("Digite o mês: "))
    dia2 = int(input("Digite o dia: "))

    print(data_recente(ano1,mes1,dia1,ano2,mes2,dia2))

def data_recente(a1,m1,d1,a2,m2,d2):
    if verifica_data(a1,m1,d1,a2,m2,d2) == False:
        return "Data inválida."
    elif a1 > a2:
        return "A primeira data é a mais recente."
    elif a1 == a2 and m1 > m2:
        return "A primeira data é a mais recente."
    elif a1 == a2 and m1 == m2 and d1 > d2:
        return "A primeira data é a mais recente."
    elif a1 == a2 and m1 == m2 and d1 == d2:
        return "As datas são iguais."
    else:
        return "A segunda data é a mais recente."

def verifica_data(a1,m1,d1,a2,m2,d2):
    if a1>2020 or a2>2020:
        return False
    if m1>12 or m1<1 or m2>12 or m2<1:
        return False
    if d1>31 or d1<1 or d2>31 or d2<1:
        return False
main()
