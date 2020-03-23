def main():
    print("\n~~~Data Atual~~~")
    ano_atual = int(input("Digite o ano atual: "))
    mes_atual = int(input("Digite o mês atual: "))
    dia_atual = int(input("Digite o dia atual: "))

    print("\n~~~Data de Nascimento~~~")
    ano_nasc = int(input("Digite o ano de nascimento: "))
    mes_nasc = int(input("Digite o mês de nascimento: "))
    dia_nasc = int(input("Digite o dia de nascimento: "))

    print(idade(ano_atual,mes_atual,dia_atual,ano_nasc,mes_nasc,dia_nasc))

def idade(aa,ma,da,an,mn,dn):
    if verifica_datas(aa,ma,da,an,mn,dn) == False:
        return "Datas inválidas."
    
    idade_ano = aa - an

    if ma < mn:
        idade_ano -= 1
        idade_mes = 12 - (mn-ma)
        if da < dn:
            idade_mes -= 1
            idade_dia = 31 - (dn-da)
        else:
            idade_dia = da - dn
    elif ma == mn:
        if da < dn:
            idade_ano -= 1
            idade_mes = 11
            idade_dia = 31 - (dn-da)
        else:
            idade_mes = 0
            idade_dia = da - dn
    else:
        idade_mes = ma - mn
        if da < dn:
            idade_mes -= 1
            idade_dia = 31 - (dn-da)
        else:
            idade_dia = da - dn

    return "A idade é: {} anos, {} meses e {} dias.".format(idade_ano,idade_mes,idade_dia)


def verifica_datas(aa,ma,da,an,mn,dn):
    if aa < an:
        return False
    if aa<0 or an<0:
        return False
    if ma<1 or ma>12 or mn<1 or mn>12:
        return False
    if da<1 or da>31 or dn<1 or dn>31:
        return False

main()
