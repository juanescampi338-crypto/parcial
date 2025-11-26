from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float

productos = []

@app.get("/")
def home():
    return {"mensaje": "API funcionando"}

@app.post("/productos")
def crear_producto(producto: Producto):
    productos.append(producto)
    return producto

@app.get("/productos")
def listar_productos():
    return productos

@app.get("/productos/{id_producto}")
def obtener_producto(id_producto: int):
    for p in productos:
        if p.id == id_producto:
            return p
    return {"error": "Producto no encontrado"}
