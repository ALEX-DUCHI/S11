from modelos.producto import Producto
from servicios.inventario import Inventario


def mostrar_menu():
    print("\n====== SISTEMA DE GESTIÓN DE INVENTARIOS ======")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Obtener producto por ID")
    print("7. Productos con bajo stock")
    print("8. Valor total del inventario")
    print("9. Ordenar productos por precio")
    print("0. Salir")



def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                producto_id = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(producto_id, nombre, cantidad, precio)

                if inventario.agregar_producto(producto):
                    print("✅ Producto agregado correctamente")
                else:
                    print("❌ Error: El ID ya existe")
            except ValueError as e:
                print(f"❌ Error de datos: {e}")

        elif opcion == "2":
            producto_id = input("ID del producto a eliminar: ")
            if inventario.eliminar_producto(producto_id):
                print("✅ Producto eliminado correctamente")
            else:
                print("❌ Producto no encontrado")

        elif opcion == "3":
            producto_id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            if inventario.actualizar_producto(producto_id, cantidad, precio):
                print("✅ Producto actualizado correctamente")
            else:
                print("❌ Producto no encontrado")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            for p in resultados:
                print(p)

        elif opcion == "5":
            for p in inventario.listar_productos():
                print(p)

        elif opcion == "6":
            producto_id = input("ID a buscar: ")
            producto = inventario.obtener_por_id(producto_id)
            if producto:
                print(producto)
            else:
                print("No encontrado")
        elif opcion == "7":
            minimo = int(input("Stock mínimo: "))
            productos = inventario.productos_bajo_stock(minimo)
            for p in productos:
               print(p)

        elif opcion == "8":
            total = inventario.calcular_valor_total_inventario()
            print(f"💰 Valor total del inventario: ${total:.2f}")
        
        elif opcion == "9":
            descendente = input("¿Descendente? (s/n): ").lower() == "s"
            productos = inventario.ordenar_por_precio(descendente)
            for p in productos:
                print(p)
        
        elif opcion == "0":
            print("Saliendo...")
            break


if __name__ == "__main__":
    main()
