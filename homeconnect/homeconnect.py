
from datetime import date


# --------------------------------------------------------
# Clase base
# --------------------------------------------------------
class Usuario:
    def __init__(self, idUsuario, nombre, correo, contrasena, tipoUsuario):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.tipoUsuario = tipoUsuario  # "comprador" o "vendedor"
        self.calificacionPromedio = 0.0

    def registrar(self):
        print(f"Usuario {self.nombre} registrado exitosamente.")

    def iniciarSesion(self):
        print(f"Inicio de sesión exitoso para {self.correo}")

    def actualizarPerfil(self, nuevoNombre=None, nuevoCorreo=None):
        if nuevoNombre:
            self.nombre = nuevoNombre
        if nuevoCorreo:
            self.correo = nuevoCorreo
        print("Perfil actualizado correctamente.")

    def cerrarSesion(self):
        print(f"El usuario {self.nombre} cerró sesión.")


# --------------------------------------------------------
# Polimorfismo aplicado: Subclases que heredan de Usuario
# --------------------------------------------------------

class Vendedor(Usuario):
    def __init__(self, idUsuario, nombre, correo, contrasena):
        super().__init__(idUsuario, nombre, correo, contrasena, "vendedor")
        self.productos = []  # agregación

    # Polimorfismo: redefinimos el método registrar()
    def registrar(self):
        print(f"Vendedor {self.nombre} registrado con perfil comercial.")

    def agregarProducto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado al catálogo de {self.nombre}.")


class Comprador(Usuario):
    def __init__(self, idUsuario, nombre, correo, contrasena):
        super().__init__(idUsuario, nombre, correo, contrasena, "comprador")
        self.compras = []

    # Polimorfismo: redefinimos el método registrar()
    def registrar(self):
        print(f"Comprador {self.nombre} registrado en el sistema.")

    def realizarCompra(self, producto):
        if producto.stock > 0:
            producto.stock -= 1
            self.compras.append(producto)
            print(f"{self.nombre} compró '{producto.nombre}'.")
        else:
            print(f"El producto '{producto.nombre}' no tiene stock disponible.")


# --------------------------------------------------------
# Clase Producto (AGREGACIÓN con Vendedor)
# --------------------------------------------------------
class Producto:
    def __init__(self, idProducto, nombre, descripcion, precio, stock, vendedor):
        self.idProducto = idProducto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        # Agregación: el producto "conoce" al vendedor pero no depende de él
        self.vendedor = vendedor
        self.calificacionPromedio = 0.0
        self.calificaciones = []

    def publicar(self):
        print(f"Producto '{self.nombre}' publicado correctamente por {self.vendedor.nombre}.")

    def editarProducto(self, nuevoPrecio=None, nuevaDescripcion=None):
        if nuevoPrecio:
            self.precio = nuevoPrecio
        if nuevaDescripcion:
            self.descripcion = nuevaDescripcion
        print(f"Producto '{self.nombre}' actualizado correctamente.")

    def eliminarProducto(self):
        print(f"Producto '{self.nombre}' eliminado del catálogo.")

    def actualizarStock(self, cantidad):
        self.stock = cantidad
        print(f"El stock de '{self.nombre}' se actualizó a {self.stock} unidades.")

    def calcularPromedioCalificaciones(self):
        if len(self.calificaciones) > 0:
            self.calificacionPromedio = sum([c.puntuacion for c in self.calificaciones]) / len(self.calificaciones)
        else:
            self.calificacionPromedio = 0.0
        return self.calificacionPromedio


# --------------------------------------------------------
# Clase Calificación (COMPOSICIÓN con Producto)
# --------------------------------------------------------
class Calificacion:
    def __init__(self, idCalificacion, producto, comprador, puntuacion, comentario):
        self.idCalificacion = idCalificacion
        # Composición: la calificación solo existe si el producto existe
        self.producto = producto
        self.comprador = comprador
        self.puntuacion = puntuacion
        self.comentario = comentario
        self.fecha = date.today()

    def registrarCalificacion(self):
        self.producto.calificaciones.append(self)
        print(f"Calificación registrada para '{self.producto.nombre}': {self.puntuacion} estrellas.")

    def editarCalificacion(self, nuevaPuntuacion=None, nuevoComentario=None):
        if nuevaPuntuacion:
            self.puntuacion = nuevaPuntuacion
        if nuevoComentario:
            self.comentario = nuevoComentario
        print("Calificación actualizada correctamente.")

    def eliminarCalificacion(self):
        if self in self.producto.calificaciones:
            self.producto.calificaciones.remove(self)
        print("Calificación eliminada correctamente.")


# --------------------------------------------------------
# Ejemplo de uso con agregación, composición y polimorfismo
# --------------------------------------------------------
if __name__ == "__main__":
    # Polimorfismo: diferentes tipos de usuario
    vendedor = Vendedor(1, "Laura", "laura@correo.com", "1234")
    comprador = Comprador(2, "Juan", "juan@correo.com", "abcd")

    # Llamadas polimórficas al método registrar()
    vendedor.registrar()
    comprador.registrar()

    # Agregación: el producto conoce a su vendedor, pero puede existir sin él
    producto = Producto(101, "Lámpara LED", "Lámpara moderna para escritorio", 120000, 10, vendedor)
    vendedor.agregarProducto(producto)
    producto.publicar()

    # Composición: la calificación depende del producto
    calificacion = Calificacion(1, producto, comprador, 5, "Excelente producto")
    calificacion.registrarCalificacion()

    # Mostrar promedio de calificaciones
    print(f"Promedio del producto '{producto.nombre}': {producto.calcularPromedioCalificaciones()} estrellas")

    # Simulación de compra
    comprador.realizarCompra(producto)
