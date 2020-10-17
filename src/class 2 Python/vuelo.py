class vuelos():
    def __init__(self,capacidad):
        self.capacidad = capacidad
        self.pasajeros = []

    def add_pasajero(self, name):

        if not self.open_seats():
            return False

        self.pasajeros.append(name)

        return True

    def open_seats(self):
        return self.capacidad - len(self.pasajeros)

vuelo= vuelos(3)

personas =["Alan", "Paco", "Pedro", "El Pepe"]

for persona in personas:

    if vuelo.add_pasajero(personas):
        print(f"{persona} fue añadido al vuelo con exito\n")
    else:
        print(f"No hay asientos disponibles para {persona}")
