import csv


def solicitar_nombre():
    while True:
        nombre = input("Nombre del alumno: ").strip()

        if nombre:
            return nombre

        print("Error: el nombre no puede estar vacío.")


def solicitar_calificacion(numero):
    while True:
        try:
            calificacion = float(input(f"Calificación {numero} (0-10): "))

            if 0 <= calificacion <= 10:
                return calificacion

            print("Error: la calificación debe estar entre 0 y 10.")

        except ValueError:
            print("Error: introduce un número válido.")


def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)


def registrar_alumno():
    nombre = solicitar_nombre()

    calificaciones = [
        solicitar_calificacion(1),
        solicitar_calificacion(2),
        solicitar_calificacion(3)
    ]

    promedio = calcular_promedio(calificaciones)
    estado = "APROBADO" if promedio >= 6 else "REPROBADO"

    return {
        "nombre": nombre,
        "calificacion1": calificaciones[0],
        "calificacion2": calificaciones[1],
        "calificacion3": calificaciones[2],
        "promedio": round(promedio, 2),
        "estado": estado
    }


def guardar_reporte(alumnos):
    with open("reporte_calificaciones.csv", "w",
              newline="", encoding="utf-8") as archivo:

        campos = [
            "nombre",
            "calificacion1",
            "calificacion2",
            "calificacion3",
            "promedio",
            "estado"
        ]

        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(alumnos)


def main():
    alumnos = []

    print("================================")
    print("     SISTEMA DE CALIFICACIONES")
    print("================================")

    while True:
        alumno = registrar_alumno()
        alumnos.append(alumno)

        continuar = input(
            "\n¿Deseas registrar otro alumno? (s/n): "
        ).strip().lower()

        if continuar != "s":
            break

    guardar_reporte(alumnos)

    aprobados = sum(
        1 for alumno in alumnos
        if alumno["estado"] == "APROBADO"
    )

    reprobados = len(alumnos) - aprobados

    promedio_general = sum(
        alumno["promedio"] for alumno in alumnos
    ) / len(alumnos)

    print("\n===== RESUMEN =====")
    print(f"Total de alumnos: {len(alumnos)}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
    print(f"Promedio general: {promedio_general:.2f}")
    print("\nReporte generado: reporte_calificaciones.csv")


if __name__ == "__main__":
    main()