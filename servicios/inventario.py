import os 
from modelos.producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self._productos_lista = []
        self._archivo = archivo
        self._cargar_desde_archivo()
        self._productos_dict = {} 
        self._nombres = set ()

    def _cargar_desde_archivo(self):
        self._productos_dict[producto.get_id()] = producto
        try:
            if not os.path.exists(self._archivo):
                open(self._archivo, "w").close()
                return

            with open(self._archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        producto = Producto.from_line(linea)
                        self._productos_dict[producto.get_id()] = producto
                        self._nombres.add(producto.get_nombre().lower())
                    except Exception:
                        continue
        except PermissionError:
            print("❌ Error: No hay permisos para leer el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al cargar archivo: {e}")
    def _guardar_en_archivo(self):
        try:
            with open(self._archivo, "w", encoding="utf-8") as f:
                for producto in self._productos:
                    f.write(producto.to_line())
            return True
        except PermissionError:
            print("❌ Error: No hay permisos para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"❌ Error inesperado al guardar archivo: {e}")
            return False

    def agregar_producto(self, producto):
        if producto.get_id() in self._productos_dict:
            return False
        if producto.get_nombre().lower() in self._nombres:
            return False
        self._nombres.add(producto.get_nombre().lower())
        self._productos_dict[producto.get_id()] = producto
        self._productos.append(producto)
        
        return self._guardar_en_archivo()
    

    def eliminar_producto(self, producto_id: int):
        for producto in self._productos:
            if producto.get_id() == producto_id:
                self._productos.remove(producto)
                return self._guardar_en_archivo()
        return False

    def actualizar_producto(self, producto_id: int, nueva_cantidad=None, nuevo_precio=None):
        for producto in self._productos:
            if producto.get_id() == producto_id:
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                return self._guardar_en_archivo()
        return False

    def buscar_por_nombre(self, nombre: str):
        nombre = nombre.lower()
        return [p for p in self._productos if nombre in p.get_nombre().lower()]

    def listar_productos(self):
        return self._productos
