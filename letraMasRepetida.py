def letraMasRepetida(textoOriginal):
    # Letra más repetida en el texto original
    letra_mas_repetida_original = ""
    max_repeticiones_original = 0
    posiciones_original = []

    for letra in textoOriginal:
        if letra == " ":
            continue
        repeticiones = 0
        posiciones = []
        for i, char in enumerate(textoOriginal):
            if char == letra:
                repeticiones += 1
                posiciones.append(i)
        if repeticiones > max_repeticiones_original:
            letra_mas_repetida_original = letra
            max_repeticiones_original = repeticiones
            posiciones_original = posiciones

    print(f"Letra mas repetida en el texto original: '{
        letra_mas_repetida_original}' en posiciones {posiciones_original}")
