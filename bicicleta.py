# bicicleta.py


class DisponibilidadInvalidaError(Exception):
    """Excepción personalizada para disponibilidad incorrecta."""
    pass


class Bicicleta:
    def __init__(self, id, marca, modelo, disponibilidad, precio):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.disponibilidad = disponibilidad
        self.precio = precio


    def mostrar_info(self):
        print(f"ID: {self.id}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Disponibilidad: {self.disponibilidad}")
        print(f"Precio: {self.precio}")


    def registrar(self):
        """Registra una bicicleta con validaciones básicas."""
        try:
            self.id = int(input("ID: "))
            self.marca = input("Marca: ").strip()
            self.modelo = input("Modelo: ").strip()


            dispo_input = input("Disponibilidad (true/false): ").lower()
            if dispo_input not in ["true", "false"]:
                raise DisponibilidadInvalidaError("Debes ingresar 'true' o 'false' para la disponibilidad.")
            self.disponibilidad = dispo_input == "true"


            self.precio = int(input("Precio: "))
            if self.precio < 0:
                raise ValueError("El precio no puede ser negativo.")


            print("Bicicleta registrada con éxito.")
            return self


        except ValueError as e:
            print(f"Error en el registro de la bicicleta: {e}")
            return None
        except DisponibilidadInvalidaError as e:
            print(f"Error: {e}")
            return None