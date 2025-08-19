# reserva.py
from bicicleta import Bicicleta
import uuid
from datetime import datetime

class FechaInvalidaError(Exception):
    """Excepción personalizada para fechas inválidas."""
    pass

class Reserva:
    def __init__(self, rut_cliente, id_reserva, id_bicicleta, fecha_inicio, fecha_termino, estado, bicicleta: Bicicleta):
        self.rut_cliente = rut_cliente
        self.id_reserva = id_reserva
        self.id_bicicleta = id_bicicleta
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.estado = estado
        self.bicicleta = bicicleta
        self.saldo = None

    def reservar(self, rut_cliente, id_bicicleta, estado):
        try:
            self.rut_cliente = input("Rut: ").strip()
            fecha_inicio_str = input("Fecha de inicio (YYYY-MM-DD): ")
            fecha_termino_str = input("Fecha de término (YYYY-MM-DD): ")
            self.estado = input("Estado: ").strip()

            # Generar ID de reserva
            self.id_reserva = str(uuid.uuid4())
            self.id_bicicleta = id_bicicleta

            # Validar fechas
            self.fecha_inicio = self._formatear_fecha(fecha_inicio_str)
            self.fecha_termino = self._formatear_fecha(fecha_termino_str)

            if self.fecha_inicio >= self.fecha_termino:
                # Uso de raise para error de negocio
                raise FechaInvalidaError("La fecha de término debe ser posterior a la fecha de inicio.")

            print(f"Reserva realizada con éxito. ID de reserva: {self.id_reserva}")
            return self

        except (ValueError, FechaInvalidaError) as e:
            print(f"Error al crear la reserva: {e}")
            return None
        finally:
            print("[LOG] Fin del proceso de creación de reserva.")

    def _formatear_fecha(self, fecha_str):
        try:
            return datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            # Re-lanzar con mensaje claro
            raise ValueError("Formato de fecha inválido. Usa YYYY-MM-DD.")

    def total_renta(self, precio, fecha_inicio, fecha_termino):
        try:
            # Cálculo en días completos; si necesitas por hora, ajusta aquí
            dias_renta = (self.fecha_termino - self.fecha_inicio).days
            if dias_renta <= 0:
                # Evita precio 0 si las fechas son el mismo día; regla mínima de 1 día
                dias_renta = 1
            precio_reserva = dias_renta * int(precio)

            if self.saldo is None:  # Solo establecer la primera vez
                self.saldo = precio_reserva

            print(f"El precio total de la reserva es: {precio_reserva}")
            return precio_reserva

        except (TypeError, ValueError) as e:
            print(f"Error al calcular total: {e}")
            return None
        finally:
            print("[LOG] Cálculo de total_renta finalizado.")

    def pagar(self, precio_reserva, monto_cancelado, saldo):
        try:
            if self.saldo is None:
                self.saldo = precio_reserva

            monto_cancelado = int(input(f"Ingrese el monto a cancelar (Saldo pendiente: {self.saldo}): "))

            if monto_cancelado == self.saldo:
                self.saldo = 0
                print("Reserva pagada completamente. Tu saldo es: 0")
            elif monto_cancelado < self.saldo:
                self.saldo -= monto_cancelado
                print(f"Monto abonado con éxito. Tu nuevo saldo es: {self.saldo}")
            else:
                print("El monto ingresado es mayor al saldo pendiente. No se puede procesar.")

            return self.saldo

        except ValueError:
            print("Debes ingresar un valor numérico.")
            return self.saldo
        finally:
            print("[LOG] Operación de pago finalizada.")

    def anular_reserva(self, id_a_anular):
        # No lanza excepción: retorna True/False para que el caller decida
        if self.id_reserva == id_a_anular:
            print("Reserva anulada con éxito.")
            return True
        else:
            print("Reserva no encontrada.")
            return False
