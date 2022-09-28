def main():
    #escribe tu código abajo de esta línea
    size=int(input())
    lista=[]
    sin_duplicados=[]
    if tam>0:
        for n in range(size):
            lista.append(input())
        for elemento in lista:
            if elemento not in sin_duplicados:
                sin_duplicados.append(elemento)
        print(lista)
        print(sin_duplicados)
    else:
        print("Error")


if __name__=='__main__':
    main()
