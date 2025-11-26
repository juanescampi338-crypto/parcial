from datetime import datetime
from typing import List


# ============================
#        Calificación
# ============================

class Calificacion:
    def __init__(self, Calificacion: int, Producto, Comprador, puntuacion: int, comentario: str, fecha: datetime = None):
        self.Calificacion = Calificacion          # int
        self.Producto = Producto                  # Producto
        self.Comprador = Comprador                # Usuario (comprador)
        self.puntuacion = puntuacion              # int (1 a 5)
        self.comentario = comentario              # String
        self.fecha = fecha if fecha else datetime.now()  # Date

    def getValor(self) -> int:
        return self.puntuacion

    def getComentario(self) -> str:
        return self.comentario

    def getFecha(self) -> datetime:
        return self.fecha

    def validarValor(self, valor: int) -> bool:
        return 1 <= valor <= 5



# ============================
#          Usuario
# ============================

class Usuario:
    def __init__(self, Usuario: int, nombre: str, correo: str, contraseña: str, tipoUsuario: str):
        self.Usuario = Usuario              # int
        self.nombre = nombre                # String
        self.correo = correo                # String
        self.contraseña = contraseña        # String
        self.tipoUsuario = tipoUsuario      # "comprador" o "vendedor"
        self.calificaciones: List[Calificacion] = []   # List<Calificacion>

    def iniciarSesion(self, correo: str, contraseña: str) -> bool:
        return self.correo == correo and self.contraseña == contraseña

    def cerrarSesion(self) -> void:
        pass

    def actualizarCorreo(self, nuevoCorreo: str) -> void:
        self.correo = nuevoCorreo

    def actualizarContraseña(self, nuevaContraseña: str) -> void:
        self.contraseña = nuevaContraseña

    def getIdUsuario(self) -> int:
        return self.Usuario

    def getNombre(self) -> str:
        return self.nombre

    def getCorreo(self) -> str:
        return self.correo

    def validarCorreo(self, correo: str) -> bool:
        return "@" in correo and "." in correo

    def encriptarContraseña(self, contraseña: str) -> str:
        return contraseña[::-1]



# ============================
#          Producto
# ============================

class Producto:
    def __init__(self, Producto: int, nombre: str, descripcion: str, precio: float, stock: int, Vendedor: int):
        self.Producto = Producto            # int
        self.nombre = nombre                # String
        self.descripcion = descripcion      # String
        self.precio = precio                # float
        self.stock = stock                  # int
        self.Vendedor = Vendedor            # int (id vendedor)
        self.calificaciones: List[Calificacion] = []  # List<Calificacion>

    def actualizarPrecio(self, nuevoPrecio: float) -> void:
        if self.validarPrecio(nuevoPrecio):
            self.precio = nuevoPrecio

    def agregarCalificacion(self, calificacion: Calificacion) -> void:
        self.calificaciones.append(calificacion)

    def obtenerCalificaciones(self) -> List[Calificacion]:
        return self.calificaciones

    def calcularPromedioCalificaciones(self) -> float:
        if not self.calificaciones:
            return 0
        return sum(c.puntuacion for c in self.calificaciones) / len(self.calificaciones)

    def validarPrecio(self, precio: float) -> bool:
        return precio > 0



# ============================
#          Vendedor
# ============================

class Vendedor(Usuario):
    def __init__(self, Usuario: int, nombre: str, correo: str, contraseña: str):
        super().__init__(Usuario, nombre, correo, contraseña, "vendedor")
        self.listaProductos: List[Producto] = []       # List<Producto>
        self.ventasRealizadas: int = 0                # int

    def agregarProducto(self, producto: Producto) -> void:
        self.listaProductos.append(producto)

    def eliminarProducto(self, idProducto: int) -> bool:
        for p in self.listaProductos:
            if p.Producto == idProducto:
                self.listaProductos.remove(p)
                return True
        return False

    def obtenerProductos(self) -> List[Producto]:
        return self.listaProductos

    def actualizarPrecio(self, idProducto: int, nuevoPrecio: float) -> bool:
        for p in self.listaProductos:
            if p.Producto == idProducto:
                p.actualizarPrecio(nuevoPrecio)
                return True
        return False

    def buscarProducto(self, idProducto: int) -> Producto:
        for p in self.listaProductos:
            if p.Producto == idProducto:
                return p
        return None



# ============================
#          Comprador
# ============================

class Comprador(Usuario):
    def __init__(self, Usuario: int, nombre: str, correo: str, contraseña: str, metodoPago: str, direccionEnvio: str):
        super().__init__(Usuario, nombre, correo, contraseña, "comprador")
        self.historialCompras: List[Producto] = []     # List<Producto>
        self.metodoPago = metodoPago                   # String
        self.direccionEnvio = direccionEnvio           # String

    def comprarProducto(self, producto: Producto) -> bool:
        if producto.stock > 0:
            producto.stock -= 1
            self.registrarCompra(producto)
            return True
        return False

    def obtenerHistorial(self) -> List[Producto]:
        return self.historialCompras

    def calificarProducto(self, producto: Producto, valor: int, comentario: str) -> Calificacion:
        calificacion = Calificacion(
            Calificacion=len(self.calificaciones) + 1,
            Producto=producto,
            Comprador=self,
            puntuacion=valor,
            comentario=comentario
        )
        producto.agregarCalificacion(calificacion)
        self.calificaciones.append(calificacion)
        return calificacion

    def registrarCompra(self, producto: Producto) -> void:
        self.historialCompras.append(producto)
