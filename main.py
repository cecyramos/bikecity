# main.py
from bicicleta import Bicicleta
from reserva import Reserva
from datetime import datetime

bicicletas = []
reservas = []

def menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar bicicleta")
    print("2. Reservar bicicleta")
    print("3. Mostrar información de bicicletas")
    print("4. Mostrar total a pagar")
    print("5. Anular reserva")
    print("6. Pagar reserva")
    print("7. Salir")

while True:
    menu()
    opcion = input("¿Qué deseas hacer? ")

    try:
        if opcion == "1":
            nueva_bicicleta = Bicicleta(0, "", "", True, 0)
            nueva_bicicleta = nueva_bicicleta.registrar()
            if nueva_bicicleta:
                bicicletas.append(nueva_bicicleta)

        elif opcion == "2":
            if not bicicletas:
                print("Primero debes registrar al menos una bicicleta.")
                continue
            try:
                bicicleta_id = int(input("Ingresa el ID de la bicicleta a reservar: "))
            except ValueError:
                print("Debes ingresar un número válido.")
                continue

            bicicleta_encontrada = next((b for b in bicicletas if b.id == bicicleta_id and b.disponibilidad), None)
            if bicicleta_encontrada:
                nueva_reserva = Reserva("", "", 0, "", "", "", bicicleta_encontrada)
                nueva_reserva = nueva_reserva.reservar("", 0, "")
                if nueva_reserva:
                    reservas.append(nueva_reserva)
                    bicicleta_encontrada.disponibilidad = False
            else:
                print("Bicicleta no disponible o no encontrada.")

        elif opcion == "3":
            if not bicicletas:
                print("No hay bicicletas registradas.")
            else:
                try:
                    id_bici = int(input("Ingresa el ID de la bicicleta que deseas consultar: "))
                    bici = next((b for b in bicicletas if b.id == id_bici), None)
                    if bici:
                        bici.mostrar_info()
                    else:
                        print("No se encontró una bicicleta con ese ID.")
                except ValueError:
                    print("Por favor ingresa un número válido como ID.")

        elif opcion == "4":
            if not reservas:
                print("No hay reservas registradas.")
                continue
            id_reserva = input("Ingresa el ID de la reserva: ")
            reserva_encontrada = next((r for r in reservas if r.id_reserva == id_reserva), None)
            if reserva_encontrada:
                reserva_encontrada.total_renta(reserva_encontrada.bicicleta.precio, reserva_encontrada.fecha_inicio, reserva_encontrada.fecha_termino)
            else:
                print("Reserva no encontrada.")

        elif opcion == "5":
            id_reserva = input("Ingresa el ID de la reserva a anular: ")
            reserva_encontrada = next((r for r in reservas if r.id_reserva == id_reserva), None)
            if reserva_encontrada:
                exito = reserva_encontrada.anular_reserva(id_reserva)
                if exito:
                    reservas.remove(reserva_encontrada)
            else:
                print("Reserva no encontrada.")

        elif opcion == "6":
            id_reserva = input("Ingresa el ID de la reserva: ")
            reserva_encontrada = next((r for r in reservas if r.id_reserva == id_reserva), None)
            if reserva_encontrada:
                precio_total = reserva_encontrada.total_renta(reserva_encontrada.bicicleta.precio, reserva_encontrada.fecha_inicio, reserva_encontrada.fecha_termino)
                reserva_encontrada.pagar(precio_total, 0, 0)
            else:
                print("Reserva no encontrada.")

        elif opcion == "7":
            print("Gracias por usar el sistema de reservas de bicicletas.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

    finally:
        print("Operación finalizada.\n")