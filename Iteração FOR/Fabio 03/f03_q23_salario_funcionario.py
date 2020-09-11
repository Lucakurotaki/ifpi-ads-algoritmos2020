def main():
    n = int(input("Digite o número de funcionários: "))

    if n == 0:
        print("Erro. Digite um valor positivo.")

    else:
        if n < 0:
            n = n*-1

        for i in range(0, n):
            print()
            cod = int(input("Insira o código do funcionário: "))
            hrs = int(input("Insira o número de horas trabalhadas: "))
            dep = int(input("Insira o número de dependentes: "))

            sb = hrs*12 + dep*40
            inss = sb*0.085
            ir = sb*0.05

            sl = sb-(inss+ir)

            print("\nCódigo de funcionário: {}\n"
                  "Descontos: INSS: R$ {:.2f}; IR: R$ {:.2f}.\n"
                  "Salário líquido: R$ {:.2f}".format(cod, inss, ir, sl))


main()
