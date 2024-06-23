from datetime import datetime

class Huesped:
    def __init__(self, nombre, documento_identificacion):
        self.nombre = nombre
        self.documento_identificacion = documento_identificacion

    def __str__(self):
        return f"Huésped: {self.nombre}, Documento: {self.documento_identificacion}"

class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.estado = 'disponible'

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}) - Estado: {self.estado}"

    def marcar_ocupada(self):
        self.estado = 'ocupada'

    def marcar_disponible(self):
        self.estado = 'disponible'

class Reserva:
    def __init__(self, huesped, habitacion, fecha_entrada, fecha_salida):
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        habitacion.marcar_ocupada()

    def __str__(self):
        return f"Reserva para {self.huesped.nombre} en {self.habitacion} desde {self.fecha_entrada} hasta {self.fecha_salida}"

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        disponibles = [hab for hab in self.habitaciones if hab.estado == 'disponible']
        for hab in disponibles:
            print(hab)

    def realizar_reserva(self, huesped, numero_habitacion, fecha_entrada, fecha_salida):
        habitacion = next((hab for hab in self.habitaciones if hab.numero == numero_habitacion and hab.estado == 'disponible'), None)
        if habitacion:
            reserva = Reserva(huesped, habitacion, fecha_entrada, fecha_salida)
            self.reservas.append(reserva)
            print(f"Reserva realizada con éxito:\n{reserva}")
        else:
            print(f"No se pudo realizar la reserva. La habitación {numero_habitacion} no está disponible.")

    def cancelar_reserva(self, huesped, numero_habitacion):
        reserva = next((res for res in self.reservas if res.huesped == huesped and res.habitacion.numero == numero_habitacion), None)
        if reserva:
            reserva.habitacion.marcar_disponible()
            self.reservas.remove(reserva)
            print(f"Reserva cancelada con éxito para la habitación {numero_habitacion} a nombre de {huesped.nombre}.")
        else:
            print(f"No se encontró una reserva para la habitación {numero_habitacion} a nombre de {huesped.nombre}.")

# Ejemplo de uso del sistema de reservas
hotel = Hotel("Hotel POO")

# Agregar habitaciones al hotel
hotel.agregar_habitacion(Habitacion(101, "simple"))
hotel.agregar_habitacion(Habitacion(102, "doble"))
hotel.agregar_habitacion(Habitacion(201, "suite"))

# Crear un huésped
huesped1 = Huesped("Juan Pérez", "12345678")

# Mostrar habitaciones disponibles antes de la reserva
print("Habitaciones disponibles antes de la reserva:")
hotel.mostrar_habitaciones_disponibles()

# Realizar una reserva
hotel.realizar_reserva(huesped1, 101, datetime(2024, 7, 1), datetime(2024, 7, 10))

# Mostrar habitaciones disponibles después de la reserva
print("\nHabitaciones disponibles después de la reserva:")
hotel.mostrar_habitaciones_disponibles()

# Cancelar una reserva
hotel.cancelar_reserva(huesped1, 101)

# Mostrar habitaciones disponibles después de cancelar la reserva
print("\nHabitaciones disponibles después de cancelar la reserva:")
hotel.mostrar_habitaciones_disponibles()