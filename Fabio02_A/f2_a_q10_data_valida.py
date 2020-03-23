def main():
    ano = int(input("Digite o ano: "))
    mes = int(input("Digite o mês: "))
    dia = int(input("Digite o dia: "))

    print(verifica_data(ano,mes,dia))

def verifica_data(ano,mes,dia):

    if ano >= 0 and mes >= 1 and mes <=12:
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia <= 31 and dia >= 1:
                return "É uma data válida."
            else:
                return "É uma data inválida."
        elif mes == 2:
            if ano%4 == 0:
                if dia <= 29 and dia >=1:
                    return "É uma data válida."
                else:
                    return "É umda data inválida."
            else:
                if dia <= 28 and dia >=1:
                    return "É uma data válida."
                else:
                    return "É umda data inválida."
        else:
            if dia <= 30 and dia >=1:
                return "É uma data válida."
            else:
                return "É uma data inválida."
    else:
        return "É uma data inválida."


main()
