class Producto:
    def __init__(self, producto_id: str, nombre: str, cantidad: int, precio: float):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        
        self._id = str(producto_id)
        self._nombre = nombre.strip()
        self._cantidad = cantidad
        self._precio = precio

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def set_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._cantidad = cantidad

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = precio
    def calcular_valor_total(self):
        return self._cantidad * self._precio

    def to_line(self):
        return f"{self._id},{self._nombre},{self._cantidad},{self._precio}\n"
    @staticmethod
    def from_line(linea):
        partes = linea.strip().split(",")
        if len(partes) != 4:
            raise ValueError("Línea corrupta en archivo")
        producto_id, nombre, cantidad, precio = partes
        return Producto(producto_id, nombre, int(cantidad), float(precio))

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"