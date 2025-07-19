class Cita:
    def __init__(self, fecha, nombre, dni, correo, telefono, examen, horario, medico):
        self.__fecha = fecha
        self.__nombre = nombre
        self.__dni = dni
        self.__correo = correo
        self.__telefono = telefono
        self.__examen = examen
        self.__horario = horario
        self.__medico = medico

    def mostrar(self):
        print(f"Fecha: {self.__fecha}")
        print(f"Nombre: {self.__nombre}")
        print(f"DNI: {self.__dni}")
        print(f"Correo: {self.__correo}")
        print(f"Teléfono: {self.__telefono}")
        print(f"Tipo de examen: {self.__examen}")
        print(f"Horario: {self.__horario}")
        print(f"Médico: Dr. {self.__medico}")

    def get_atributo(self, campo):
        return getattr(self, f"_Cita__{campo}", "")

    def set_atributo(self, campo, valor):
        if hasattr(self, f"_Cita__{campo}"):
            setattr(self, f"_Cita__{campo}", valor)
