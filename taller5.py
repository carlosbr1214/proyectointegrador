def clasificar_funcionamiento(puntuacion):
    if puntuacion == 2:
        return "Defectuoso"
    elif puntuacion == 3:
        return "Moderado"
    else:
        return "Óptimo"

cabinas = []

for i in range(4):
    puntuacion = int(input(f"Ingrese puntaje para la cabina {i+1}: "))
    cabinas.append((i+1, puntuacion))

for cabina, puntuacion in cabinas:
    funcionamiento = clasificar_funcionamiento(puntuacion)
    print(f"Cabina {cabina}: Puntuación = {puntuacion}, Funcionamiento: {funcionamiento}")