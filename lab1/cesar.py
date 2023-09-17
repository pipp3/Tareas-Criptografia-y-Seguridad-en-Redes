import sys

def cifrar_cesar(texto, corrimiento):
    texto_cifrado = ""

    for char in texto:
        # Comprobamos si el carácter es una letra del alfabeto
        if char.isalpha():
            # Determinamos si es una letra mayúscula o minúscula
            if char.isupper():
                inicio = ord('A')
            else:
                inicio = ord('a')

            # Aplicamos el cifrado César
            posicion_original = ord(char) - inicio
            nueva_posicion = (posicion_original + corrimiento) % 26
            char_cifrado = chr(inicio + nueva_posicion)
        else:
            # Si no es una letra, dejamos el carácter sin cambios
            char_cifrado = char

        texto_cifrado += char_cifrado

    return texto_cifrado

def main():
    if len(sys.argv) != 3:
        print("Uso: python programa.py <texto_a_cifrar> <corrimiento>")
        sys.exit(1)

    texto_a_cifrar = sys.argv[1]
    corrimiento = int(sys.argv[2])

    texto_cifrado = cifrar_cesar(texto_a_cifrar, corrimiento)
    print("Texto cifrado:", texto_cifrado)

if __name__ == "__main__":
    main()

