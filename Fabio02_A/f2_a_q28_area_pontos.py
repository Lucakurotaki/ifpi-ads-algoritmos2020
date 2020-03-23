def main():
    x1 = int(input("Digite o valor do eixo x do ponto A: "))
    y1 = int(input("Digite o valor do eixo y do ponto A: "))
    x2 = int(input("Digite o valor do eixo x do ponto B: "))
    y2 = int(input("Digite o valor do eixo y do ponto B: "))

    print(area(x1,y1,x2,y2))

def area(x1,y1,x2,y2):

    if x1 > x2:
        base = x1 - x2
    elif x2 > x1:
        base = x2 - x1
    else:
        return "Os valores do eixo x precisam ser diferentes."

    if y1 > y2:
        altura = y1 - y2
    elif y2 > y1:
        altura = y2 - y1
    else:
        return
    "Os valores do eixo y precisam ser diferentes."

    area = base*altura

    return "A área do retângulo formado por dois pontos é: {} m².".format(area)

main()
