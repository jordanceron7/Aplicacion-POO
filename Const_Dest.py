class SesionUsuario:
    def __init__(self, nombre, correo):
        """
        Constructor de la clase.
        Se ejecuta automáticamente al crear el objeto.
        Inicializa los atributos del usuario.
        """
        self.nombre = nombre
        self.correo = correo
        print(f"Sesión iniciada para el usuario: {self.nombre}")

    def mostrar_datos(self):
        """
        Método que muestra la información del usuario.
        """
        print("Datos del usuario:")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta cuando el objeto es eliminado
        o cuando el programa finaliza.
        Se utiliza para liberar recursos.
        """
        print(f"Sesión finalizada para el usuario: {self.nombre}")


# Programa principal
if __name__ == "__main__":
    # Creación del objeto (llamada al constructor)
    usuario1 = SesionUsuario("Jordan Cerón", "jordan07@outlook.com")

    # Uso de los métodos del objeto
    usuario1.mostrar_datos()

    # Eliminación del objeto (llamada al destructor)
    del usuario1

    print("Programa finalizado")
