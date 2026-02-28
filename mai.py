from modelos.producto import Producto
from servicios.inventario import Inventario


def mostrar_menu():
    print("\n====== SISTEMA DE GESTIÓN DE INVENTARIOS ======")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")
    print("7. Productos con bajo stock")
    print("8. Valor total del inventario")



def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        elif opcion == "7":
        minimo = int(input("Stock mínimo: "))
        productos = inventario.productos_bajo_stock(minimo)
        for p in productos:
         print(p)
         
        elif opcion == "8":
        total = inventario.calcular_valor_total_inventario()
        print(f"💰 Valor total del inventario: ${total:.2f}")

        if opcion == "1":
            try:
                pid = input("ID del producto: ").strip()
                nombre = input("Nombre: ").strip()
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(pid, nombre, cantidad, precio)

                if inventario.agregar_producto(producto):
                    print("✅ Producto agregado correctamente")
                else:
                    print("❌ Error: El ID ya existe")
            except ValueError as e:
                print(f"❌ Error de datos: {e}")

        elif opcion == "2":
            pid = input("ID del producto a eliminar: ").strip()
            if inventario.eliminar_producto(pid):
                print("✅ Producto eliminado correctamente")
            else:
                print("❌ Producto no encontrado")

        elif opcion == "3":
            try:
                pid = input("ID del producto a actualizar: ").strip()
                cantidad = input("Nueva cantidad (Enter para omitir): ").strip()
                precio = input("Nuevo precio (Enter para omitir): ").strip()

                nueva_cantidad = int(cantidad) if cantidad else None
                nuevo_precio = float(precio) if precio else None

                if inventario.actualizar_producto(pid, nueva_cantidad, nuevo_precio):
                    print("✅ Producto actualizado correctamente")
                else:
                    print("❌ Producto no encontrado")
            except ValueError as e:
                print(f"❌ Error de datos: {e}")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ").strip()
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                print("\n Resultados encontrados:")
                for producto in resultados:
                    print(producto)
            else:
                print("❌ No se encontraron productos")

        elif opcion == "5":
            productos = inventario.listar_productos()
            if productos:
                print("\n📋 Inventario actual:")
                for producto in productos:
                    print(producto)
            else:
                print("📦 Inventario vacío")

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida, intente nuevamente")


if __name__ == "__main__":
    main()
