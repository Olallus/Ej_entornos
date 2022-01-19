frase = input("Introduzca una frase: ")
intentos = int(input("Dime los intentos permitidos: "))
contador = 0
longitud = len(frase)
contmal = 0
listapal = []
listaintentos = []
listafrase = []
listapalabras = []
palabrasseparadas = frase.split(" ")
palabras = 1
fraseintento = []
listanumpalabras = []
palabrastotal = 0
for letrita in frase:
    listapal.append(letrita)
    if letrita == " ":
        palabras = palabras + 1
while intentos > 0:
    num_palabras = int(input("Adivine numero de palabras: "))
    listanumpalabras.append(num_palabras)
    if palabras < num_palabras:
        intentos = intentos - 1
        print("El número a adivinar es menor.", intentos, "Intentos restantes")
    elif palabras > num_palabras:
        intentos = intentos - 1
        print("El número a adivinar es mayor.", intentos, "Intentos restantes")
    elif intentos == 0:
        print("Te has quedado sin intentos, la frase correcta era", frase)
        break
    else:
        print("Ha acertado el número! La frase tiene ")
        print(num_palabras, " palabras")
        int2 = intentos - 1
        intentos = 0
while int2 > 0:
    print("¿Que quieres adivinar?")
    op = int(input("Pulse 2 para letra, 1 para palabra y 0 para frase "))
    if op == 2:
        letras_faltan = 0
        variab = ""
        letra_adivinada = input("Dime una letra")
        listaintentos.append(letra_adivinada)
        for letra in frase:
            contar = 0
            if letra in listaintentos:
                variab = variab + letra
                contar = contar + 1
                if len(variab) == len(frase):
                    print("Si existe la letra.", variab)
            elif letra == " ":
                variab = variab + " "
            else:
                variab = variab + "+"
                letras_faltantes = letras_faltan + 1
            if len(variab) == len(frase):
                int2 = int2 - 1
                print("No existe la letra.", variab)
                print(int2, "Intentos restantes")
            elif int2 == 0:
                print("Te has quedado sin intentos, la frase era ", frase)
                print("Los intentos numero de letras fueron los siguientes: ")
                print(listanumpalabras)
                print("Los intentos de letras fueron los siguientes:")
                print(listaintentos)
                print("Los intentos de palabras fueron los siguientes:")
                print(listapalabras)
                print("Los intentos de frase fueron los siguientes: ")
                print(fraseintento)
                break

    elif op == 1:
        palab = input("Dime una palabra: ")
        listapalabras.append(palab)
        for palabr in palabrasseparadas:
            if palabr in listapalabras:
                print("Si existe la palabra ", palab)
            else:
                palabrastotal = palabrastotal + 1
                if palabrastotal == num_palabras:
                    print("No existe la palabra.", int2, "Intentos restantes")
    else:
        fraseintento = input("Dime una frase: ")
        if fraseintento == frase:
            print("La frase es la correcta!")
            print("Los intentos numero de letras fueron los siguientes: ")
            print(listanumpalabras)
            print("Los intentos de letras fueron los siguientes:")
            print(listaintentos)
            print("Los intentos de palabras fueron los siguientes:")
            print(listapalabras)
            print("Los intentos de frase fueron los siguientes: ")
            print(fraseintento)
            break
        else:
            listafrase.append(fraseintento)
            int2 = int2 - 1
            print("Frase incorrecta.", int2, "Intentos restantes")
