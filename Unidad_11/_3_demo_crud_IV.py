# Demo proyecto
# Refactorizamos el código del archivo "_7_class_act_2.py" de la carpeta "Unidad_5" 
# para generar el CRUD de la entidad producto

# Importamos librerias externas
from tabulate import tabulate
import re

# Declaramos la variable global (se pueden cargar algunos registros para inicializarla)
productos = [
    {
        "id_producto": 1,
        "categoria": "Escritura",
        "nombre": "Lápiz negro HB",
        "precio_unitario": 350,
    },
    {
        "id_producto": 2,
        "categoria": "Escritura",
        "nombre": "Bolígrafo azul",
        "precio_unitario": 500,
    },
]

# Declaramos la estructura del diccionario producto:
producto = {"categoria": None, "nombre": None, "precio_unitario": None}


# Funcion validar categoria
# Parametros: categoria:string
# Retorno: True if OK o False:bool
def validar_categoria(categoria):
    patron_categoria = r"[A-Za-záéíóúÁÉÍÓÚüÜñÑ\s]+"
    return bool(re.fullmatch(patron_categoria, categoria.strip()))


# Funcion validar nombre
# Parametros: nombre:string
# Retorno: True if OK o False:bool
def validar_nombre(nombre):
    patron_nombre = r"[A-Za-z0-9áéíóúÁÉÍÓÚüÜñÑ ]+"
    return bool(re.fullmatch(patron_nombre, nombre.strip()))


# Funcion validar precio_unitario
# Parametros: precio_unitario:str
# Retorno: True if OK o False:bool
def validar_precio_unitario(precio_unitario):
    patron = r"[0-9]+(\.[0-9]{1,2})?"
    return bool(re.fullmatch(patron, precio_unitario.strip()))

# Funcion leer consola
# Parametros: none
# Retorno: diccionario producto
def leer_producto():
    # Ingresar categoria
    while True:
        categoria = input("Ingrese la categoria: ")
        if validar_categoria(categoria):
            break
        print("Categoría no válido intente nuevamente...")

    # Ingresar nombre
    while True:
        nombre = input("Ingrese el nombre: ")
        if validar_nombre(nombre):
            break
        print("Nombre no válido intente nuevamente...")

    # Ingresar precio_unitario
    while True:
        precio_unitario = input("Ingrese el precio unitario: ")
        if validar_precio_unitario(precio_unitario):
            break
        print("Precio no válido intente nuevamente...")

    # Normalizacion y carga en variable temporal
    producto = {
        "categoria": categoria.strip().title(),
        "nombre": nombre.strip().title(),
        "precio_unitario": float(precio_unitario.strip()),
    }

    return producto


# Funcion generar id_producto
def generar_id_producto():
    if not productos:  # lista vacía
        return 1

    max_id = max(productos, key=lambda p: p["id_producto"])
    return max_id["id_producto"] + 1


# Funcion persistir producto
def persistir_producto(producto):
    producto["id_producto"] = generar_id_producto()
    productos.append(producto)
    return True


# Funcion get_producto_by_id
# Parametros: id_producto:int
# Retorno: productos:list
def get_producto_by_id(id_producto):
    # Búsqueda con lista por comprensión
    productos_found = [producto for producto in productos if re.fullmatch(str(id_producto), str(producto["id_producto"]))]
    return productos_found

# Funcion get_producto_by_nombre
# Parametros: nombre:str
# Retorno: productos_encontrados:list
def get_producto_by_nombre(nombre):
    # Búsqueda con lista por comprensión
    productos_found = [producto for producto in productos if re.search(nombre, producto["nombre"], re.IGNORECASE)]
    # Retornamos la lista, vacía o con los registros encontrados
    return productos_found


# Funcion Principal
def main():
    print("Bienvenido!!")

    while True:
        print(
            """
    Ingrese:
    1. Para crear un nuevo producto
    2. Para listar todos los productos
    3. Para buscar producto por id_producto
    4. Para buscar producto por nombre de producto
    5. Para salir
            """
        )
        opcion = input("Ingrese su opción: ")
        match opcion:
            case "1":
                # Alta de producto
                producto = leer_producto()
                response = persistir_producto(producto)
                print("Producto insertado exitosamente") if response else None

            case "2":
                # Listar productos
                print(tabulate(productos[:5], headers="keys", tablefmt="grid"))

            case "3":
                id_producto = int(input("Ingrese el id_producto a buscar: "))
                productos_found = get_producto_by_id(id_producto)
                if productos_found:
                    print(tabulate(productos_found, headers="keys", tablefmt="grid"))
                else:
                    print("No match")
            case "4":
                nombre = input("Ingrese el nombre del producto a buscar - total o parcial: ")
                productos_found = get_producto_by_nombre(nombre)
                print(tabulate(productos_found[:5], headers="keys", tablefmt="grid"))
            case "5":
                # Terminar App
                print("Saliendo...")
                break
            case _:
                print("Opción inválida, intente nuevamente...")


# Invocar a la función principal
if __name__ == "__main__":
    main()
