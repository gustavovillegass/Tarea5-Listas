def main():
    cantidad=int(input('Dime la cantidad de valores que hay en la lista, '))
    lista=[]

    for num in range(cantidad):
        lista.append(int(input('Dime cada uno de los valores, ')))

    for cont in range(len(lista)):
        if lista[cont] % 2 == 0:
            print("pos "+ str(cont) + ", valor "+ str(lista[cont]))


if __name__=='__main__':
    main()
