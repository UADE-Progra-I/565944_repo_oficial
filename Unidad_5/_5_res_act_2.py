"""
CONSIGNA:
Generar una función principal y luego subfunciones que sean invocadas desde la función principal,
de manera de mantener el mismo workflow de la actividad_1, pero aprovechando las ventajas
de trabajar módulos reutilixables.

1. Imprimir un mensaje de bienvenida
2. Leer el nombre de un estudiante por consola
3. Verificar que sea un nombre válido
4. Si es válido guardarlo en la lista global
5. Si es inválido, mostrar un mensaje en la consola
6. A fin de poder repetir el flujo, incluir el código dentro de un bucle while

"""

# Declaramos una lista global para almacenar los nombres de los estudiantes
estudiantes = []

# Funcion principal
def main():
    # Cuerpo de la funcion principal

    while True:
        # Mostrar mensaje de bienvenida
        mensaje_bienvenida()

        # Leer nombre
        nombre = leer_estudiante()

        # Validar nombre
        check = validar_nombre(nombre)

        # Accion en funcion de check
        if check:
            agregar_estudiante(nombre)
            print(f"Estudiante agregado exitosamente!\n")
            mostrar_estudiantes()
        else:
            print(f"Nombre inválido!\n")
        
        # Continua o termina?
        action = input("Ingrese cualquier tecla para continuar o 's' para salir: ")
        if action.lower() == 's':
            break
    
    print("Gracias por usar nuestra APP")

# Funcion mensaje de bienvenida
def mensaje_bienvenida():
    print("Bienvenido al sistema de gestión de estudiantes.\n")

# Funcion leer el nombre de un estudiante por consola
def leer_estudiante():
    nombre = input("Ingrese su nombre: ")
    return nombre

# Funcion verificar que sea un nombre válido
# Retorna True si es valido o Falso si no lo es
def validar_nombre(nombre):
    return True if nombre.strip() != "" else False

# Funcion agregar estudiante a la lista
def agregar_estudiante(nombre):
    estudiantes.append(nombre)

# Funcion que lista los estudiante
def mostrar_estudiantes():
    for index, estudiante in enumerate(estudiantes):
        print(f"{index}: {estudiante}")

# Llamada a función main
if __name__ == "__main__":
    main()