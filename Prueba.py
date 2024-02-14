import datetime as fecha_actual

ordenes = []

seguir=True

def AGREGARORDEN(fecha, cliente, tipo, precio=None, referencia=None):
    nueva_orden = {
        "fecha": fecha,
        "cliente": cliente,
        "tipo": tipo
    }

    if tipo == "1" :
        nueva_orden["precio"] = precio
    elif tipo == "2":
        nueva_orden["referencia"] = referencia

    ordenes.append(nueva_orden)
    print("Orden agregada exitosamente.")

def BUSCARPORCLIENTE(cliente):
    return [orden for orden in ordenes if orden['cliente'] == cliente]



def ACTUALIZARORDEN(orden, nueva_fecha):
    orden['fecha'] = nueva_fecha
    print("Orden actualizada exitosamente.")


def MOSTRARORDEN():
    for orden in ordenes:
        print(orden)
        print(f"Fecha: {orden['fecha']}, Cliente: {orden['cliente']}, Tipo: {orden['tipo']}")

def ELIMINARORDEN(orden):
    ordenes.remove(orden)
    print("Orden eliminada exitosamente.")

while True:
    print("\n--------------MENU-------------")
    print("1. Ingresar una orden")
    print("2. Mostrar todas las órdenes")
    print("3. Actualizar una orden")
    print("4. Eliminar una orden")
    print("5. Salir")

    opcion = int(input("Ingrese la opción: "))

    if opcion == 1:
        fecha_orden = input("Ingrese la fecha de la orden: ")
        cliente_orden = input("Ingrese el nombre del cliente: ")
        tipo_orden = input("Ingrese el tipo de orden (1.normal o 2.garantia): ")

        if tipo_orden == "1":
            precio_orden = float(input("Ingrese el precio de la orden normal: "))
            AGREGARORDEN(fecha_orden, cliente_orden, tipo_orden, precio=precio_orden)
        elif tipo_orden == "2":
            referencia_orden = input("Ingrese la referencia para la orden de garantía: ")
            AGREGARORDEN(fecha_orden, cliente_orden, tipo_orden, referencia=referencia_orden)
        else:
            print("Opción no válida.")
            continue

    elif opcion == 2:
        MOSTRARORDEN()

    elif opcion == 3:
        cliente_a_actualizar = input("Ingrese el nombre del cliente para actualizar la orden: ")
        ordenes_cliente = BUSCARPORCLIENTE(cliente_a_actualizar)

        if not ordenes_cliente:
            print(f"No se encontraron órdenes para el cliente {cliente_a_actualizar}.")
            continue

        nueva_fecha = input("Ingrese la nueva fecha: ")
        for orden in ordenes_cliente:
            ACTUALIZARORDEN(orden, nueva_fecha)

            
    elif opcion == 4:
        MOSTRARORDEN()
        cliente_a_eliminar = input("Ingrese el nombre del cliente para eliminar la orden: ")
        ordenes_cliente = BUSCARPORCLIENTE(cliente_a_eliminar)

        if not ordenes_cliente:
            print(f"No se encontraron órdenes para el cliente {cliente_a_eliminar}.")
            continue

        for orden in ordenes_cliente:
            ELIMINARORDEN(orden)

    elif opcion == 5:
        print(" Hasta luego.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")