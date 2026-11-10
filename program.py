def es_anagrama(palabra1, palabra2):
    # Limpiar espacios y convertir a minusculas
    p1 = palabra1.lower().replace(" ", "")
    p2 = palabra2.lower().replace(" ", "")

    return sorted(p1) == sorted(p2)

print(es_anagrama("Roma", "Amor"))
print(es_anagrama("casa", "mesa"))