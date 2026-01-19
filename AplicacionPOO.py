# Clase base que representa un dispositivo de red genérico
class Dispositivo:
    def __init__(self, hostname, ip):
        self._hostname = hostname   # atributo protegido (encapsulación)
        self._ip = ip               # atributo protegido

    # Método que será sobreescrito por las clases derivadas
    def procesar_paquete(self):
        return f"{self._hostname} recibe un paquete."

    # Método común para mostrar información
    def obtener_info(self):
        return f"Hostname: {self._hostname}, IP: {self._ip}"


# Clase derivada que representa un Router
class Router(Dispositivo):
    def __init__(self, hostname, ip, rutas):
        super().__init__(hostname, ip)
        self._rutas = rutas   # tabla de rutas simulada

    # Polimorfismo: comportamiento específico al procesar paquetes
    def procesar_paquete(self):
        return f"{self._hostname} reenvía paquetes según la tabla de rutas."

    # Método particular de Router
    def obtener_info(self):
        return f"{super().obtener_info()}, Rutas configuradas: {len(self._rutas)}"


# Clase derivada que representa un Servidor
class Servidor(Dispositivo):
    def __init__(self, hostname, ip, servicio):
        super().__init__(hostname, ip)
        self._servicio = servicio   # servicio ofrecido

    # Polimorfismo: sobrescritura
    def procesar_paquete(self):
        return f"{self._hostname} procesa solicitudes del servicio {self._servicio}."

    def obtener_info(self):
        return f"{super().obtener_info()}, Servicio: {self._servicio}"


# Instanciación de objetos
dispositivo = Dispositivo("Switch-01", "192.168.1.10")
router = Router("Router-Core", "192.168.1.1", ["0.0.0.0/0", "192.168.0.0/16"])
server = Servidor("Server-Web", "192.168.1.100", "HTTP")

# Demostración polimórfica
dispositivos = [dispositivo, router, server]

for d in dispositivos:
    print(d.obtener_info())
    print(d.procesar_paquete())
    print("-----------------------")
