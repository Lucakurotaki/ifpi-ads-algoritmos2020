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
    
    idade_anos = aa - an
    if ma - mn > 0:
        return "\nTem {} anos de idade.".format(idade_anos)
    elif ma == mn and da - dn >= 0:
        return "\nTem {} anos de idade.".format(idade_anos)
    else:
        return "\nTem {} anos de idade.".format(idade_anos - 1)

main()
        
