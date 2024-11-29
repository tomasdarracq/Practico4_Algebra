import numpy as np


def CriptoSistema2(texto, T, b):
    texto = texto.lower()

    letrasDiccionario = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
        'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
        'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '*': 28
    }

    numerosDiccionario = {v: k for k, v in letrasDiccionario.items()}

    while len(texto) % 3 != 0:
        texto += ' '

    bloques = []
    i = 0
    while i < len(texto):
        bloques.append(texto[i:i + 3])
        i += 3

    vectores = []
    for bloque in bloques:
        vector = []
        for char in bloque:
            vector.append(letrasDiccionario[char])
        vectores.append(np.array(vector).reshape(-1, 1))

    vectores_encriptados = []
    for vector in vectores:
        encriptado = (np.dot(T, vector) + b) % 29
        vectores_encriptados.append(encriptado)

    texto_encriptado = ''
    for vector in vectores_encriptados:
        for num in vector:
            texto_encriptado += numerosDiccionario[int(num[0])]

    return texto_encriptado


def DesencriptaCriptoSistema2(texto_encriptado, T_inv, b):
    texto_encriptado = texto_encriptado.lower()

    letrasDiccionario = {
        'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
        'm': 12, 'n': 13, 'ñ': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22,
        'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '*': 28
    }

    numerosDiccionario = {v: k for k, v in letrasDiccionario.items()}

    bloques = []
    i = 0
    while i < len(texto_encriptado):
        bloques.append(texto_encriptado[i:i + 3])
        i += 3

    vectores_encriptados = []
    for bloque in bloques:
        vector = []
        for char in bloque:
            vector.append(letrasDiccionario[char])
        vectores_encriptados.append(np.array(vector).reshape(-1, 1))

    vectores_desencriptados = []
    for vector in vectores_encriptados:
        desencriptado = np.dot(T_inv, (vector - b)) % 29
        vectores_desencriptados.append(desencriptado)

    texto_desencriptado = ''
    for vector in vectores_desencriptados:
        for num in vector:
            texto_desencriptado += numerosDiccionario[int(num[0])]

    return texto_desencriptado


# Función para calcular la inversa modular de una matriz
def inversa_modular_matriz(T, mod):
    det = int(round(np.linalg.det(T))) % mod
    adj = np.round(det * np.linalg.inv(T)).astype(int) % mod
    det_inv = None
    for i in range(1, mod):
        if (det * i) % mod == 1:
            det_inv = i
            break
    if det_inv is None:
        raise ValueError("El determinante no tiene inverso modular")
    T_inv = (det_inv * adj) % mod
    return T_inv
