import sys
import subprocess
import time
import struct

def send_ping_message(message):
    sequence = 1  # Inicializar la secuencia en 1

    for char in message:
        char_byte = ord(char) & 0xFF  # Obtener el byte menos significativo del carácter
        icmp_type = 8  # Tipo de paquete ICMP: 8 para Echo Request
        icmp_code = 0  # Código ICMP: 0 para Echo Request
        icmp_checksum = 0  # El valor del checksum se calculará automáticamente

        # Estructura del paquete ICMP Echo Request
        packet = struct.pack("BBHHH", icmp_type, icmp_code, icmp_checksum, sequence, 0)
        packet = packet + bytes([char_byte]) + b'\x00' * (56 - len(packet))
        
        ping_command = f"ping -c 1 -p {packet.hex()} 8.8.8.8"
        subprocess.run(ping_command, shell=True)
        time.sleep(1)  # Esperar 1 segundo entre paquetes
        sequence = (sequence + 1) % 256  # Incrementar la secuencia y limitarla a 0-255

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 enviar_ping.py <mensaje>")
        sys.exit(1)

    mensaje = sys.argv[1]
    send_ping_message(mensaje)
