#diccionarios de sinonimos
sinonimos = {
    'feliz': ['contento', 'alegre', 'satisfecho', 'dichoso'],
    'triste': ['afligido', 'melancólico', 'deprimido', 'desdichado'],
    'rápido': ['veloz', 'ligero', 'acelerado', 'precipitado'],
    'lento': ['pausado', 'despacio', 'tardío', 'perezoso'],
    'grande': ['enorme', 'gigante', 'extenso', 'amplio'],
    'pequeño': ['diminuto', 'minúsculo', 'reducido', 'compacto']
}
def buscar_sinonimos(palabra):
    palabra = palabra.lower()
    if palabra in sinonimos:
        return sinonimos[palabra]
    else:
        return f'No se encontraron sinónimos para "{palabra}".'
palabra = input("Introduce una palabra para buscar sinónimos: ")
resultado = buscar_sinonimos(palabra)
if isinstance(resultado, list):
        print(f"Sinónimos de {palabra}: {', '.join(resultado)}")
else:
        print(resultado)
