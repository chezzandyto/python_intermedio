#guarda en la lista los cuadrados del 1 al 100 solo los que no son divisibles para 3

def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1,101) if i%3 != 0]

    print(squares)

    #reto

    lista = [i for i in range(1,99999) if i%36 == 0]
    print(lista)

if __name__ == '__main__':
    run()