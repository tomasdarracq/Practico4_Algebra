def CriptoSistema1(palabraAEncriptar, a, b):

    palabraAEncriptar = palabraAEncriptar.lower()

    # Diccionario para convertir letras a números
    letrasDiccionario = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
        'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
        'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '*': 28
    }

    # Diccionario inverso para convertir números a letras
    numerosDiccionario = {}
    for letra, numero in letrasDiccionario.items():
        numerosDiccionario[numero] = letra

    # Convertir cada letra a su número correspondiente
    numeros = []
    for char in palabraAEncriptar:
        numeros.append(letrasDiccionario[char])

    # Encriptar cada número usando  E(x) = (a * x + b) % 29
    encriptados = []
    for num in numeros:
        encriptados.append((a * num + b) % 29)

    # Convertir los números encriptados de vuelta a letras
    textoEncriptado = ""
    for num in encriptados:
        textoEncriptado += numerosDiccionario[num]

    return textoEncriptado


def DesencriptaCriptoSistema1(textoEncriptado, a, b):

    textoEncriptado = textoEncriptado.lower()

    # Diccionario para convertir letras a números
    letrasDiccionario = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
        'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
        'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '*': 28
    }

    # Diccionario inverso para convertir números a letras
    numerosDiccionario = {}
    for letra, numero in letrasDiccionario.items():
        numerosDiccionario[numero] = letra

    # Encontrar el inverso modular de a en módulo 29
    a_inverso = None
    for x in range(1, 29):  # un número tal que (a * x) % 29 == 1
        if (a * x) % 29 == 1:
            a_inverso = x
            break

    if a_inverso is None:
        raise ValueError("No se encontró el inverso modular de 'a'")

    # Convertir cada letra del texto encriptado a su número correspondiente
    numerosEncriptados = []
    for char in textoEncriptado:
        numerosEncriptados.append(letrasDiccionario[char])

    # Desencriptar cada número usando la fórmula D(x) = a_inverso * (x - b) % 29
    desencriptados = []
    for num in numerosEncriptados:
        desencriptados.append((a_inverso * (num - b)) % 29)

    # Convertir los números desencriptados de vuelta a letras
    textoDesencriptado = ""
    for num in desencriptados:
        textoDesencriptado += numerosDiccionario[num]

    return textoDesencriptado
