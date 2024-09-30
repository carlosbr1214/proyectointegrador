def clasificar_leucemia(puntuacion):
    if puntuacion < 20:
        return "Bajo riesgo"
    elif puntuacion < 50:
        return "Riesgo intermedio"
    else:
        return "Alto riesgo"

pacientes = [int(input(f"Ingrese puntuación de leucemia para el paciente {i+1}: ")) for i in range(8)]

for i, puntuacion in enumerate(pacientes, start=1):
    riesgo = clasificar_leucemia(puntuacion)
    print(f"Paciente {i}: Puntuación = {puntuacion}, Nivel de riesgo: {riesgo}")