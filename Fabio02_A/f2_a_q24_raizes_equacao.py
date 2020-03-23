def main():
    print("y = ax²+bx+c")
    a = int(input('Insira o valor do coeficiente "a": '))
    b = int(input('Insira o valor do coeficiente "b": '))
    c = int(input('Insira o valor do coeficiente "c": '))

    print(raizes(a,b,c))

def raizes(a,b,c):

    if a == 0:
        return 'O coeficiente "a" deve ser diferente de 0.'
    delta = b**2 - 4*a*c
    r_delta = delta**(1/2)

    if delta > 0:
        x1 = (-b+r_delta)/(2*a)
        x2 = (-b-r_delta)/(2*a)
        return "As raízes da equação são: {:.2} e {:.2}.".format(x1,x2)
    elif delta == 0:
        x = -b/(2*a)
        return "A raíz da equação é: {:.2}.".format(x)
    else:
        return "Não há raízes reais."

main()
