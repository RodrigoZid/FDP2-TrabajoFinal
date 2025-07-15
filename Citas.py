class Cita:
    def __init__(self, fecha, nombre, dni, medico, horario, correo, telefono, examen):
        self._fecha = fecha
        self._nombre = nombre
        self._dni = dni
        self._medico = medico
        self._horario = horario
        self._correo = correo
        self._telefono = telefono
        self._examen = examen

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, valor):
        self._fecha = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor):
        self._dni = valor

    @property
    def medico(self):
        return self._medico

    @medico.setter
    def medico(self, valor):
        self._medico = valor

    @property
    def horario(self):
        return self._horario

    @horario.setter
    def horario(self, valor):
        self._horario = valor


    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        self._correo = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor

    @property
    def examen(self):
        return self._examen

    @examen.setter
    def examen(self, valor):
        self._examen = valor
