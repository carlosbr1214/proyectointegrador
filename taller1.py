def main():
    numero_actual = 5
    numeros = []

    contador = 0
    while contador < 100:
        if numero_actual != 13:
            numeros.append(numero_actual)
        numero_actual += 4
        contador += 1

    print("Los primeros 100 números de la serie omitiendo el 13 son:")
    for numero in numeros:
        print(numero)

if __name__ == "__main__":
    main()








