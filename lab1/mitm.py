import pyshark

# Función para descifrar un texto cifrado en César con un corrimiento dado
def cesar_decrypt(texto_cifrado, corrimiento):
    texto_descifrado = ""
    for char in texto_cifrado:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            descifrado_char = chr(((ord(char) - offset - corrimiento) % 26) + offset)
            texto_descifrado += descifrado_char
        else:
            texto_descifrado += char
    return texto_descifrado

# Analizar el archivo de captura de Wireshark
def analizar_captura(captura_file):
    cap = pyshark.FileCapture(captura_file)

    for pkt in cap:
        if "ICMP" in pkt:
            try:
                data_hex = pkt.icmp.data
                # Decodificar datos hexadecimales a texto
                data_text = bytes.fromhex(data_hex).decode('utf-8')
                print(f"Datos ICMP cifrados: {data_text}")

                # Probar todas las combinaciones posibles de corrimiento
                for corrimiento in range(1, 26):
                    texto_descifrado = cesar_decrypt(data_text, corrimiento)
                    print(f"Corrimiento {corrimiento}: {texto_descifrado}")
            except AttributeError:
                # El paquete ICMP no tiene datos o no es texto
                pass

if __name__ == "__main__":
    captura_file = "ping2.pcapng"  # Reemplaza con el nombre de tu archivo de captura
    analizar_captura(captura_file)


