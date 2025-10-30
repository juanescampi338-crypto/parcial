from datetime import date

class Persona:
    def __init__(self, nombre: str, nif: str, fecha_nac: date):
        self.nombre = nombre
        self.nif = nif
        self.fecha_nac = fecha_nac

class Jugador(Persona):
    def __init__(self, nombre: str, nif: str, fecha_nac: date, num_fed: int):
        super().__init__(nombre, nif, fecha_nac)
        self.num_fed = num_fed
