import re
from Citas import Cita

 
# Función para validar el DNI (solo números y 8 dígitos)
def validar_dni(dni):
    if not dni.isdigit() or len(dni) != 8:
        raise ValueError("El DNI debe ser un número de 8 dígitos.")
    return dni

def registrar_cita(lista_citas, horarios, medicos, horarios_disponibles, tipos_examen):
    fecha = input("\nIngrese la fecha deseada para la cita (formato dd/mm/aaaa): ")
    nombre = input("Ingrese el nombre del paciente: ")
    
    # Validación del DNI
    while True:
        dni = input("Ingrese el DNI del paciente: ")
        try:
            dni = validar_dni(dni)
            break
        except ValueError as e:
            print(e)

 
    correo = input("Ingrese el correo electrónico del paciente: ")
    telefono = input("Ingrese el número de teléfono del paciente: ")

    print("\nSeleccione el tipo de examen a realizar:")
    for i, examen in enumerate(tipos_examen, start=1):
        print(f"{i}. {examen}")
    while True:
        try:
            opcion_examen = int(input("Ingrese una opción: "))
            if 1 <= opcion_examen <= len(tipos_examen):
                examen = tipos_examen[opcion_examen - 1]
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

    while True:
        print("\nElija un horario disponible:\n")
        for i, disponible in enumerate(horarios_disponibles):
            if disponible:
                print(f"{i+1}. {horarios[i]}")
        try:
            opcion = int(input("Seleccione una opción: "))
            if 1 <= opcion <= len(horarios) and horarios_disponibles[opcion - 1]:
                horario = horarios[opcion - 1]
                medico = medicos[opcion - 1]
                horarios_disponibles[opcion - 1] = False
                lista_citas.append(Cita(fecha, nombre, dni, medico, horario, correo, telefono, examen))
                print("\n¡Cita registrada exitosamente!")
                print("\n--- Detalles de la cita ---")
                print(f"Fecha: {fecha}")
                print(f"Nombre: {nombre}")
                print(f"DNI: {dni}")
                print(f"Correo: {correo}")
                print(f"Teléfono: {telefono}")
                print(f"Tipo de examen: {examen}")
                print(f"Horario: {horario}")
                print(f"Médico: Dr. {medico}")
                print("\nSe enviará un recordatorio a su correo electrónico 24 horas antes de su cita.")
                print("Se ha enviado una encuesta a su correo electrónico.")
                return
            else:
                print("Opción inválida o no disponible.")
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

def mostrar_citas(lista_citas):
    if not lista_citas:
        print("\nNo hay citas registradas.")
        return
    print("\nCitas registradas:")
    for i, cita in enumerate(lista_citas, start=1):
        print(f"\nCita #{i}:")
        print(f"Fecha: {cita.fecha}")
        print(f"Nombre: {cita.nombre}")
        print(f"DNI: {cita.dni}")
        print(f"Correo: {cita.correo}")
        print(f"Teléfono: {cita.telefono}")
        print(f"Tipo de examen: {cita.examen}")
        print(f"Horario: {cita.horario}")
        print(f"Médico: Dr. {cita.medico}")

def mostrar_horarios_disponibles(horarios, disponibles):
    print("\nHorarios disponibles:")
    for i, disponible in enumerate(disponibles):
        if disponible:
            print(f"{i+1}. {horarios[i]}")

def buscar_por_campo(lista_citas, campo, valor):
    encontrados = [c for c in lista_citas if getattr(c, campo).lower() == valor.lower()]
    if not encontrados:
        print("\nNo se encontraron citas.")
        return
    for i, cita in enumerate(encontrados, start=1):
        print(f"\nCita #{i}:")
        print(f"Fecha: {cita.fecha}")
        print(f"Nombre: {cita.nombre}")
        print(f"DNI: {cita.dni}")
        print(f"Correo: {cita.correo}")
        print(f"Teléfono: {cita.telefono}")
        print(f"Tipo de examen: {cita.examen}")
        print(f"Horario: {cita.horario}")
        print(f"Médico: Dr. {cita.medico}")

def modificar_cita(lista_citas, horarios, medicos, disponibles, tipos_examen):
    mostrar_citas(lista_citas)
    try:
        num = int(input("\nSeleccione el número de la cita a modificar: ")) - 1
        if not (0 <= num < len(lista_citas)):
            print("Número inválido.")
            return
        cita = lista_citas[num]

        if input("¿Desea cambiar la fecha? (s/n): ").lower() == 's':
            cita.fecha = input("Nueva fecha: ")

        if input("¿Desea cambiar el nombre? (s/n): ").lower() == 's':
            cita.nombre = input("Nuevo nombre: ")

        if input("¿Desea cambiar el DNI? (s/n): ").lower() == 's':
            while True:
                dni = input("Nuevo DNI: ")
                try:
                    dni = validar_dni(dni)
                    cita.dni = dni
                    break
                except ValueError as e:
                    print(e)

        if input("¿Desea cambiar el correo electrónico? (s/n): ").lower() == 's':
            while True:
                correo = input("Nuevo correo: ")
                try:
                    correo = validar_correo(correo)
                    cita.correo = correo
                    break
                except ValueError as e:
                    print(e)

        if input("¿Desea cambiar el número de teléfono? (s/n): ").lower() == 's':
            cita.telefono = input("Nuevo número: ")

        if input("¿Desea cambiar el tipo de examen? (s/n): ").lower() == 's':
            print("\nTipos de examen disponibles:")
            for i, examen in enumerate(tipos_examen, start=1):
                print(f"{i}. {examen}")
            while True:
                try:
                    nuevo_examen = int(input("Seleccione una opción: "))
                    if 1 <= nuevo_examen <= len(tipos_examen):
                        cita.examen = tipos_examen[nuevo_examen - 1]
                        break
                    else:
                        print("Opción inválida.")
                except ValueError:
                    print("Entrada inválida.")

        if input("¿Desea cambiar el horario? (s/n): ").lower() == 's':
            for i, h in enumerate(horarios):
                if h == cita.horario:
                    disponibles[i] = True
            mostrar_horarios_disponibles(horarios, disponibles)
            nuevo = int(input("Seleccione nuevo horario: ")) - 1
            if disponibles[nuevo]:
                cita.horario = horarios[nuevo]
                cita.medico = medicos[nuevo]
                disponibles[nuevo] = False
            else:
                print("Horario no disponible.")
        print("\nCita modificada.")
    except ValueError:
        print("Entrada inválida.")

def eliminar_cita(lista_citas, horarios, disponibles):
    mostrar_citas(lista_citas)
    try:
        num = int(input("\nNúmero de la cita a eliminar: ")) - 1
        if not (0 <= num < len(lista_citas)):
            print("Número inválido.")
            return
        cita = lista_citas.pop(num)
        for i, h in enumerate(horarios):
            if h == cita.horario:
                disponibles[i] = True
        print("Cita eliminada.")
    except ValueError :
        print("Entrada inválida.")

        
def main():
    horarios = ["09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
    medicos = ["Carlos Pérez", "Lucía Gómez", "Mario Rivas", "Ana Salazar",
               "Carlos Pérez", "Lucía Gómez", "Ana Salazar",
               "Carlos Pérez", "Mario Rivas", "Mario Rivas"]
    horarios_disponibles = [True] * len(horarios)
    lista_citas = []
    tipos_examen = [
        "Examen de Agudeza Visual (cartilla de Snellen)",
        "Examen de Refracción (graduación de lentes)",
        "Examen de Campo Visual",
        "Test de Daltonismo (Ishihara)"
    ]

    while True:
        print("\n--- GESTIÓN DE CITAS ---")
        print("1. Registrar nueva cita")
        print("2. Mostrar citas")
        print("3. Horarios disponibles")
        print("4. Buscar citas")
        print("5. Modificar cita")
        print("6. Eliminar cita")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            registrar_cita(lista_citas, horarios, medicos, horarios_disponibles, tipos_examen)
        elif opcion == '2':
            mostrar_citas(lista_citas)
        elif opcion == '3':
            mostrar_horarios_disponibles(horarios, horarios_disponibles)
        elif opcion == '4':
            campo = input("\nBuscar por (fecha/nombre/dni/medico/correo/telefono/examen): ").strip().lower()
            valor = input(f"Ingrese el valor de {campo}: ")
            if campo in ['fecha', 'nombre', 'dni', 'medico', 'correo', 'telefono', 'examen']:
                buscar_por_campo(lista_citas, campo, valor)
            else:
                print("Campo inválido.")
        elif opcion == '5':
            modificar_cita(lista_citas, horarios, medicos, horarios_disponibles, tipos_examen)
        elif opcion == '6':
            eliminar_cita(lista_citas, horarios, horarios_disponibles)
        elif opcion == '7':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
