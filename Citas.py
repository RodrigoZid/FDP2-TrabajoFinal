class Cita:
    def __init__(self, fecha, nombre, dni, medico, horario, correo, telefono, examen):
        self.__fecha = fecha
        self.__nombre = nombre
        self.__dni = dni
        self.__medico = medico
        self.__horario = horario
        self.__correo = correo
        self.__telefono = telefono
        self.__examen = examen

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        self.__fecha = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        self.__dni = valor

    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self, valor):
        self.__medico = valor

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, valor):
        self.__horario = valor


    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        self.__correo = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        self.__telefono = valor

    @property
    def examen(self):
        return self.__examen

    @examen.setter
    def examen(self, valor):
        self.__examen = valor
