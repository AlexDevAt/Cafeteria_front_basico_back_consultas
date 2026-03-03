from pydantic import BaseModel
from datetime import date
from decimal import Decimal


# =========================================================
# 3) CONSULTAS AVANZADAS
# =========================================================

class PedidoConAlumnoOut(BaseModel):
    nombre: str
    fecha: date
    id_pedido: int
    total: Decimal


class ProductoVendidoOut(BaseModel):
    id_pedido: int
    id_producto: int
    producto: str
    cantidad: int


class ProductoMayorPromedioOut(BaseModel):
    nombre: str
    precio: Decimal


class AlumnoConPedidoOut(BaseModel):
    nombre: str


# =========================================================
# 4) AGREGADOS
# =========================================================

class CountPedidosOut(BaseModel):
    numero_de_pedidos: int


class TotalIngresosOut(BaseModel):
    total_ingresos: Decimal


class StatsPreciosProductoOut(BaseModel):
    promedio: Decimal
    mas_caro: Decimal
    mas_barato: Decimal


class ComprasPorAlumnoOut(BaseModel):
    id_alumno: int
    nombre: str
    compras_realizadas: int


class AlumnoMasDeUnPedidoOut(BaseModel):
    id_alumno: int
    pedidos: int