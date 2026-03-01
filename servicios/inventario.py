import os 
from modelos.producto import Producto


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self._archivo = archivo
        self._productos_lista = []
        self._productos_dict = {} 
        self._nombres = set ()
        self._cargar_desde_archivo()

    def _cargar_desde_archivo(self):
        if not os.path.exists(self._archivo):
            open(self._archivo, "w").close()
            return 
        with open(self._archivo, "r", encoding="utf-8") as f:
            for linea in f:
                    try:
                        producto = Producto.from_line(linea)
                        self._productos_lista.append(producto)
                        self._productos_dict[producto.get_id()] = producto
                        self._nombres.add(producto.get_nombre().lower())
                    except:
                        continue
    def _guardar_en_archivo(self):
            with open(self._archivo, "w", encoding="utf-8") as f:
                for producto in self._productos_lista:
                    f.write(producto.to_line())

    def agregar_producto(self, producto):
        if producto.get_id() in self._productos_dict:
            return False
        if producto.get_nombre().lower() in self._nombres:
            return False
        
        self._nombres.add(producto.get_nombre().lower())
        self._productos_dict[producto.get_id()] = producto
        self._productos_lista.append(producto)
        self._guardar_en_archivo()
        
        return True
    

    def eliminar_producto(self, producto_id: str):
        if producto_id not in self._productos_dict:
              return False
        producto = self._productos_dict[producto_id]
        self._productos_lista.remove(producto)
        del self._productos_dict[producto_id]
        self._nombres.remove(producto.get_nombre().lower())
        self._guardar_en_archivo()
        return True

    def actualizar_producto(self, producto_id: str, nueva_cantidad=None, nuevo_precio=None):
        if producto_id not in self._productos_dict:
            return False

        producto = self._productos_dict[producto_id]

        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)
        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)

        self._guardar_en_archivo()
        return True

    def buscar_por_nombre(self, nombre: str):
        nombre = nombre.lower()
        return [p for p in self._productos_lista if nombre in p.get_nombre().lower()]
    
    def productos_bajo_stock(self, minimo: int):
        return [p for p in self._productos_lista if p.get_cantidad() <= minimo]
    
    def calcular_valor_total_inventario(self):
        return sum(p.calcular_valor_total() for p in self._productos_lista)
    
    def ordenar_por_precio(self, descendente=False):
        return sorted(self._productos_lista, key=lambda p: p.get_precio(), reverse=descendente)
    
    def listar_productos(self):
        return self._productos_lista
    
    def obtener_por_id(self, producto_id: str):
        return self._productos_dict.get(producto_id)
