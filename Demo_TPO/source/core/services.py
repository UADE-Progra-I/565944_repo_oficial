import re
from shared import utilities



# Funcion generar id_producto
def generar_id_producto(productos):
    if not productos:  # lista vacía
        return 1

    max_id = max(productos, key=lambda p: p["id_producto"])
    return max_id["id_producto"] + 1


# Funcion persistir producto
def crear_producto(productos, producto):
    producto["id_producto"] = generar_id_producto(productos)
    productos.append(producto)
    return True


# Funcion get_producto_by_id
# Parametros: id_producto:int
# Retorno: productos:list
def get_producto_by_id(productos, id_producto):
    # Búsqueda con lista por comprensión
    productos_found = [producto for producto in productos if re.fullmatch(str(id_producto), str(producto["id_producto"]))]
    return productos_found

# Funcion get_producto_by_nombre
# Parametros: nombre:str
# Retorno: productos_encontrados:list
def get_producto_by_nombre(productos, nombre):
    # Búsqueda con lista por comprensión
    productos_found = [producto for producto in productos if re.search(nombre, producto["nombre"], re.IGNORECASE)]
    # Retornamos la lista, vacía o con los registros encontrados
    return productos_found