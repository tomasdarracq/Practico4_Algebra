def CriptoSistema1(palabraAEncriptar, a, b):
    palabraAEncriptar = palabraAEncriptar.lower()

    letrasDiccionario = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
        'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
        'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '*': 28
    }

    numerosDiccionario = {v: k for k, v in letrasDiccionario.items()}

    numeros = [letrasDiccionario[char] for char in palabraAEncriptar]

    encriptados = [(a * num + b) % 29 for num in numeros]

    textoEncriptado = "".join(numerosDiccionario[num] for num in encriptados)
    return textoEncriptado


def DesencriptaCriptoSistema1(textoEncriptado, a, b):
    textoEncriptado = textoEncriptado.lower()

    letrasDiccionario = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
        'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
        'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '*': 28
    }

    numerosDiccionario = {v: k for k, v in letrasDiccionario.items()}

    a_inverso = None
    for x in range(1, 29):
        if (a * x) % 29 == 1:
            a_inverso = x
            break

    numerosEncriptados = [letrasDiccionario[char] for char in textoEncriptado]

    desencriptados = [(a_inverso * (num - b)) %
                      29 for num in numerosEncriptados]

    textoDesencriptado = "".join(
        numerosDiccionario[num] for num in desencriptados)
    return textoDesencriptado
