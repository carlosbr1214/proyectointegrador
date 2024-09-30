import random

# Definimos los parámetros
num_empleados = 1897
salario_base = 1000  # Salario base por empleado
comision_porcentaje = 0.10  # 10% de comision
seguridad_social_porcentaje = 0.05  # 5% de seguridad social

# Generamos datos para los empleados
empleados = []
for i in range(num_empleados):
    empleado_id = i + 1
    comision = salario_base * comision_porcentaje
    seguridad_social = salario_base * seguridad_social_porcentaje
    salario_total = salario_base + comision - seguridad_social
    empleados.append({
        'ID': empleado_id,
        'Salario Base': salario_base,
        'Comisión': comision,
        'Seguridad Social': seguridad_social,
        'Salario Total': salario_total
    })

# Imprimimos el listado de información
print(f"{'ID':<5} {'Salario Base':<15} {'Comisión':<10} {'Seguridad Social':<20} {'Salario Total':<15}")
print("="*75)

for empleado in empleados:
    print(f"{empleado['ID']:<5} {empleado['Salario Base']:<15} {empleado['Comisión']:<10} {empleado['Seguridad Social']:<20} {empleado['Salario Total']:<15}")

