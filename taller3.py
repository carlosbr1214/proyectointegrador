# Inicializamos contadores
cantidad_pares = 0
cantidad_impares = 0

# Listas para almacenar los resultados
resultados = []

# Recolección de 400 números
for i in range(400):
    while True:
        try:
            numero = int(input(f"Ingrese el número {i + 1}: "))
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

    # Determinamos si es par o impar
    if numero % 2 == 0:
        resultados.append((numero, "par"))
        cantidad_pares += 1
    else:
        resultados.append((numero, "impar"))
        cantidad_impares += 1

# Imprimir resultados
print("\nListado de números y su clasificación:")
print(f"{'Número':<10} {'Clasificación':<10}")
print("=" * 25)

for numero, clasificacion in resultados:
    print(f"{numero:<10} {clasificacion:<10}")

# Imprimir conteo final
print("\nResumen:")
print(f"Números pares: {cantidad_pares}")
print(f"Números impares: {cantidad_impares}")
