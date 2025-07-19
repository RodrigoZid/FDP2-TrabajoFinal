import re
from datetime import datetime
from Cita import Cita

class SistemaCitas:
    def __init__(self):
        self.horarios = ["09:00", "10:00", "11:00", "12:00", "13:00",
                         "14:00", "15:00", "16:00", "17:00", "18:00"]
        self.medicos = ["Carlos Pérez", "Lucía Gómez", "Mario Rivas", "Ana Salazar",
                        "Carlos Pérez", "Lucía Gómez", "Ana Salazar",
                        "Carlos Pérez", "Mario Rivas", "Mario Rivas"]
        self.horarios_disponibles = [True] * len(self.horarios)
        self.lista_citas = []
        self.tipos_examen = [
            "Examen de Agudeza Visual (cartilla de Snellen)",
            "Examen de Refracción (graduación de lentes)",
            "Examen de Campo Visual",
            "Test de Daltonismo (Ishihara)"
        ]

    def validar_fecha(self, fecha):
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def validar_dni(self, dni):
        return dni.isdigit() and len(dni) == 8

    def validar_telefono(self, telefono):
        return telefono.isdigit() and len(telefono) == 9

    def validar_correo(self, correo):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, correo) is not None

    def registrar_cita(self):
        while True:
            fecha = input("\nIngrese la fecha deseada para la cita (formato dd/mm/aaaa): ")
            if not self.validar_fecha(fecha):
                print("Fecha inválida. Use el formato dd/mm/aaaa.")
                continue
            break

        while True:
            nombre = input("Ingrese el nombre del paciente: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            break

        while True:
            dni = input("Ingrese el DNI del paciente (8 dígitos): ")
            if not self.validar_dni(dni):
                print("DNI inválido. Debe tener 8 dígitos numéricos.")
                continue
            break

        while True:
            correo = input("Ingrese el correo electrónico del paciente: ").strip()
            if not self.validar_correo(correo):
                print("Correo electrónico inválido.")
                continue
            break

        while True:
            telefono = input("Ingrese el número de teléfono del paciente (9 dígitos): ")
            if not self.validar_telefono(telefono):
                print("Teléfono inválido. Debe tener 9 dígitos numéricos.")
                continue
            break

        print("\nSeleccione el tipo de examen a realizar:")
        for i, examen in enumerate(self.tipos_examen, start=1):
            print(f"{i}. {examen}")
        while True:
            try:
                opcion_examen = int(input("Ingrese una opción: "))
                if 1 <= opcion_examen <= len(self.tipos_examen):
                    examen = self.tipos_examen[opcion_examen - 1]
                    break
                else:
                    print("Opción inválida.")
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")

        while True:
            print("\nElija un horario disponible:\n")
            for i, disponible in enumerate(self.horarios_disponibles):
                if disponible:
                    print(f"{i + 1}. {self.horarios[i]}")
            try:
                opcion = int(input("Seleccione una opción: "))
                if 1 <= opcion <= len(self.horarios) and self.horarios_disponibles[opcion - 1]:
                    horario = self.horarios[opcion - 1]
                    medico = self.medicos[opcion - 1]
                    self.horarios_disponibles[opcion - 1] = False
                    nueva_cita = Cita(fecha, nombre, dni, correo, telefono, examen, horario, medico)
                    self.lista_citas.append(nueva_cita)
                    print("\n¡Cita registrada exitosamente!")
                    print("\n====== Detalles de la cita ======")
                    nueva_cita.mostrar()
                    print("\nSe enviará un recordatorio a su correo electrónico 24 horas antes de su cita.")
                    print("Se ha enviado una encuesta a su correo electrónico.")
                    return
                else:
                    print("Opción inválida o no disponible.")
            except ValueError:
                print("Entrada inválida. Intente nuevamente.")

    def mostrar_citas(self):
        if not self.lista_citas:
            print("\nNo hay citas registradas.")
            return
        print("\nCitas registradas:")
        for i, cita in enumerate(self.lista_citas, start=1):
            print(f"\nCita #{i}:")
            cita.mostrar()

    def mostrar_horarios_disponibles(self):
        print("\nHorarios disponibles:")
        for i, disponible in enumerate(self.horarios_disponibles):
            if disponible:
                print(f"{i+1}. {self.horarios[i]}")

    def buscar_por_campo(self, campo, valor):
        encontrados = [c for c in self.lista_citas if c.get_atributo(campo).lower() == valor.lower()]
        if not encontrados:
            print("\nNo se encontraron citas.")
            return
        for i, cita in enumerate(encontrados, start=1):
            print(f"\nCita #{i}:")
            cita.mostrar()

    def modificar_cita(self):
        self.mostrar_citas()
        try:
            num = int(input("\nSeleccione el número de la cita a modificar: ")) - 1
            if not (0 <= num < len(self.lista_citas)):
                print("Número inválido.")
                return
            cita = self.lista_citas[num]

            if input("¿Desea cambiar la fecha? (s/n): ").lower() == 's':
                while True:
                    nueva_fecha = input("Nueva fecha (dd/mm/aaaa): ")
                    if self.validar_fecha(nueva_fecha):
                        cita.set_atributo("fecha", nueva_fecha)
                        break
                    else:
                        print("Fecha inválida. Intente nuevamente.")

            if input("¿Desea cambiar el nombre? (s/n): ").lower() == 's':
                while True:
                    nuevo_nombre = input("Nuevo nombre: ").strip()
                    if nuevo_nombre:
                        cita.set_atributo("nombre", nuevo_nombre)
                        break
                    else:
                        print("El nombre no puede estar vacío.")

            if input("¿Desea cambiar el DNI? (s/n): ").lower() == 's':
                while True:
                    nuevo_dni = input("Nuevo DNI (8 dígitos): ")
                    if self.validar_dni(nuevo_dni):
                        cita.set_atributo("dni", nuevo_dni)
                        break
                    else:
                        print("DNI inválido.")

            if input("¿Desea cambiar el correo electrónico? (s/n): ").lower() == 's':
                while True:
                    nuevo_correo = input("Nuevo correo: ").strip()
                    if self.validar_correo(nuevo_correo):
                        cita.set_atributo("correo", nuevo_correo)
                        break
                    else:
                        print("Correo inválido.")

            if input("¿Desea cambiar el número de teléfono? (s/n): ").lower() == 's':
                while True:
                    nuevo_telefono = input("Nuevo teléfono (9 dígitos): ")
                    if self.validar_telefono(nuevo_telefono):
                        cita.set_atributo("telefono", nuevo_telefono)
                        break
                    else:
                        print("Teléfono inválido.")

            if input("¿Desea cambiar el tipo de examen? (s/n): ").lower() == 's':
                print("\nTipos de examen disponibles:")
                for i, examen in enumerate(self.tipos_examen, start=1):
                    print(f"{i}. {examen}")
                while True:
                    try:
                        nuevo_examen = int(input("Seleccione una opción: "))
                        if 1 <= nuevo_examen <= len(self.tipos_examen):
                            cita.set_atributo("examen", self.tipos_examen[nuevo_examen - 1])
                            break
                        else:
                            print("Opción inválida.")
                    except ValueError:
                        print("Entrada inválida.")

            if input("¿Desea cambiar el horario? (s/n): ").lower() == 's':
                for i, h in enumerate(self.horarios):
                    if h == cita.get_atributo("horario"):
                        self.horarios_disponibles[i] = True
                self.mostrar_horarios_disponibles()
                while True:
                    try:
                        nuevo = int(input("Seleccione nuevo horario: ")) - 1
                        if self.horarios_disponibles[nuevo]:
                            cita.set_atributo("horario", self.horarios[nuevo])
                            cita.set_atributo("medico", self.medicos[nuevo])
                            self.horarios_disponibles[nuevo] = False
                            break
                        else:
                            print("Horario no disponible.")
                    except (ValueError, IndexError):
                        print("Entrada inválida. Intente nuevamente.")
            print("\nCita modificada.")
        except ValueError:
            print("Entrada inválida.")

    def eliminar_cita(self):
        self.mostrar_citas()
        try:
            num = int(input("\nNúmero de la cita a eliminar: ")) - 1
            if not (0 <= num < len(self.lista_citas)):
                print("Número inválido.")
                return
            cita = self.lista_citas.pop(num)
            for i, h in enumerate(self.horarios):
                if h == cita.get_atributo("horario"):
                    self.horarios_disponibles[i] = True
            print("Cita eliminada.")
        except ValueError:
            print("Entrada inválida.")

    def menu(self):
        while True:
            print("\n====== GESTIÓN DE CITAS ======")
            print("1. Registrar nueva cita")
            print("2. Mostrar citas")
            print("3. Horarios disponibles")
            print("4. Buscar citas")
            print("5. Modificar cita")
            print("6. Eliminar cita")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                self.registrar_cita()
            elif opcion == '2':
                self.mostrar_citas()
            elif opcion == '3':
                self.mostrar_horarios_disponibles()
            elif opcion == '4':
                campo = input("\nBuscar por (fecha/nombre/dni/medico/correo/telefono/examen): ").strip().lower()
                valor = input(f"Ingrese el valor de {campo}: ")
                if campo in ['fecha', 'nombre', 'dni', 'medico', 'correo', 'telefono', 'examen']:
                    self.buscar_por_campo(campo, valor)
                else:
                    print("Campo inválido.")
            elif opcion == '5':
                self.modificar_cita()
            elif opcion == '6':
                self.eliminar_cita()
            elif opcion == '7':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    sistema = SistemaCitas()
    sistema.menu()
