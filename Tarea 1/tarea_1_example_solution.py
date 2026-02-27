def filtrar_vocales(cadena, bandera):
    """
    Método: filtrar_vocales
    Parámetros de entrada:
    - cadena: texto que se va a analizar. Debe ser un string,
        solo puede contener letras y no puede estar vacío,
        ni tener más de 30 caracteres.
    - bandera: valor booleano (True o False).
        * Si es True, el método devuelve solo las vocales.
        * Si es False, devuelve solo las consonantes.
    Salida:
    - Retorna una tupla con dos valores:
        (codigo, resultado)
    - codigo: indica si hubo error o si todo salió bien.
    - resultado: string con las letras filtradas o None si hubo error.
    """
    # Códigos de retorno para identificar cada tipo de error
    ERROR_TIPO_CADENA = -100
    ERROR_SOLO_LETRAS = -200
    ERROR_CADENA_VACIA = -300
    ERROR_LONGITUD = -400
    ERROR_TIPO_BANDERA = -500
    EXITO = 0
    # Verificar que "cadena" realmente sea un string
    if not isinstance(cadena, str):
        return ERROR_TIPO_CADENA, None
    # Verificar que la cadena no esté vacía
    if cadena == "":
        return ERROR_CADENA_VACIA, None
    # Verificar que no tenga más de 30 caracteres
    if len(cadena) > 30:
        return ERROR_LONGITUD, None
    # Verificar que solo tenga letras
    if not cadena.isalpha():
        return ERROR_SOLO_LETRAS, None
    # Verifico que la bandera sea un booleano
    if not isinstance(bandera, bool):
        return ERROR_TIPO_BANDERA, None
    # Defino todas las vocales (mayúsculas y minúsculas)
    vocales = "aeiouAEIOU"
    # Si la bandera es True, filtro solo las vocales
    if bandera:
        resultado = "".join(c for c in cadena if c in vocales)
    # Si la bandera es False, filtro solo las consonantes
    else:
        resultado = "".join(c for c in cadena if c not in vocales)
    # Si todo salió bien, retorno código de éxito y el resultado
    return EXITO, resultado


def encontrar_extremos(lista_numeros):
    """
    Método: encontrar_extremos
    Parámetro de entrada:
    - lista_numeros: debe ser una lista con números (int o float).
        No puede estar vacía, no puede tener más de 15 elementos
        y no debe contener valores booleanos.
    Salida:
    - Retorna tres valores (codigo, minimo, maximo):
    - codigo: indica si hubo error o si todo salió bien.
    - minimo: número más pequeño de la lista (o None si hay error).
    - maximo: número más grande de la lista (o None si hay error).
    """
    # Códigos de retorno para los posibles errores
    ERROR_TIPO_LISTA = -600
    ERROR_SOLO_NUMEROS = -700
    ERROR_LISTA_VACIA = -800
    ERROR_LONGITUD_LISTA = -900
    EXITO = 0
    # Verificar que el parámetro recibido sea una lista
    if not isinstance(lista_numeros, list):
        return ERROR_TIPO_LISTA, None, None
    # Verificar que la lista no esté vacía
    if not lista_numeros:
        return ERROR_LISTA_VACIA, None, None
    # Verificar que no haya valores booleanos (True/False)
    if any(isinstance(x, bool) for x in lista_numeros):
        return ERROR_SOLO_NUMEROS, None, None
    # Verificar que todos los elementos sean números (int o float)
    if not all(isinstance(x, (int, float)) for x in lista_numeros):
        return ERROR_SOLO_NUMEROS, None, None
    # Verificar que no tenga más de 15 elementos
    if len(lista_numeros) > 15:
        return ERROR_LONGITUD_LISTA, None, None
    # Inicializar el mínimo y máximo con el primer valor de la lista
    # para luego ir comparando
    max_num = lista_numeros[0]
    min_num = lista_numeros[0]
    # Recorre toda la lista para encontrar el menor y el mayor
    for num in lista_numeros:
        # Si encuentro un número mayor al máximo actual, lo actualizo
        if num > max_num:
            max_num = num
        # Si encuentro un número menor al mínimo actual, lo actualizo
        if num < min_num:
            min_num = num
    # Si todo salió bien, retorno el código de éxito y los valores encontrados
    return EXITO, min_num, max_num
