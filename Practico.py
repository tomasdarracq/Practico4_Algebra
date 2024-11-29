import numpy as np
from CriptoSistema1 import CriptoSistema1, DesencriptaCriptoSistema1
from CriptoSistema2 import CriptoSistema2, DesencriptaCriptoSistema2, inversa_modular_matriz
from letraMasRepetida import letraMasRepetida

# Criptosistema 1
textoOriginal = "la culpa es de catarina"
a = 3
b = 7

textoEncriptado1 = CriptoSistema1(textoOriginal, a, b)
print("Texto encriptado (CriptoSistema1):", textoEncriptado1)

textoDesencriptado1 = DesencriptaCriptoSistema1(textoEncriptado1, a, b)
print("Texto desencriptado (CriptoSistema1):", textoDesencriptado1)

letraMasRepetida(textoOriginal)
letraMasRepetida(textoEncriptado1)

# Uso del CriptoSistema2
# Matriz T y su inversa
T = np.array([[2, 1, 0],
              [1, 1, 1],
              [0, 0, 1]])

T_inv = inversa_modular_matriz(T, 29)
# T_inv = np.linalg.inv(T).astype(int) % 29


# Vector b
b = np.array([[3], [5], [7]])

# Texto original
textoOriginal2 = "la culpa es de catarina y catarina es una espia"

# Encriptar el texto
texto_encriptado2 = CriptoSistema2(textoOriginal2, T, b)
print("Texto encriptado (CriptoSistema2):", texto_encriptado2)

# Desencriptar el texto
texto_desencriptado2 = DesencriptaCriptoSistema2(texto_encriptado2, T_inv, b)
print("Texto desencriptado (CriptoSistema2):", texto_desencriptado2)

letraMasRepetida(textoOriginal2)
letraMasRepetida(texto_encriptado2)
