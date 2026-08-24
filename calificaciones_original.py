print("SISTEMA DE CALIFICACIONES")

nombre = input("Nombre del alumno: ")
a = float(input("Calificacion 1: "))
b = float(input("Calificacion 2: "))
c = float(input("Calificacion 3: "))

promedio = (a + b + c) / 3

if promedio >= 6:
    print(nombre, "APROBADO")
else:
    print(nombre, "REPROBADO")

print("Promedio:", promedio)

nombre2 = input("Nombre del segundo alumno: ")
a2 = float(input("Calificacion 1: "))
b2 = float(input("Calificacion 2: "))
c2 = float(input("Calificacion 3: "))

promedio2 = (a2 + b2 + c2) / 3

if promedio2 >= 6:
    print(nombre2, "APROBADO")
else:
    print(nombre2, "REPROBADO")

print("Promedio:", promedio2)