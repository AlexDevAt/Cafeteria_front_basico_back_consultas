from fastapi import APIRouter, HTTPException
from repository import RepoCafeteria
from cafeteria_models import *

router = APIRouter(
    prefix="/cafeteria",
    tags=["Cafeteria"]
)

repo = RepoCafeteria()

# =========================================================
# 3) CONSULTAS AVANZADAS
# =========================================================

@router.get(
    "/avanzadas/pedidos-con-alumno",
    response_model=list[PedidoConAlumnoOut],
    status_code=200
)
def pedidos_con_alumno():
    try:
        return repo.pedidosConAlumno()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/avanzadas/productos-vendidos-por-pedido",
    response_model=list[ProductoVendidoOut],
    status_code=200
)
def productos_vendidos_por_pedido():
    try:
        return repo.productosVendidosPorPedido()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/avanzadas/productos-mayor-al-promedio",
    response_model=list[ProductoMayorPromedioOut],
    status_code=200
)
def productos_mayor_al_promedio():
    try:
        return repo.productosMayorAlPromedio()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/avanzadas/alumnos-con-pedidos",
    response_model=list[AlumnoConPedidoOut],
    status_code=200
)
def alumnos_con_pedidos():
    try:
        return repo.alumnosQueHanRealizadoPedido()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# =========================================================
# 4) AGREGADOS
# =========================================================

@router.get(
    "/agregados/count-pedidos",
    response_model=CountPedidosOut,
    status_code=200
)
def count_pedidos():
    try:
        return repo.countPedidos()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/agregados/sum-total-ingresos",
    response_model=TotalIngresosOut,
    status_code=200
)
def sum_total_ingresos():
    try:
        return repo.sumTotalIngresos()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/agregados/stats-precios-producto",
    response_model=StatsPreciosProductoOut,
    status_code=200
)
def stats_precios_producto():
    try:
        return repo.statsPreciosProducto()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/agregados/compras-por-alumno",
    response_model=list[ComprasPorAlumnoOut],
    status_code=200
)
def compras_por_alumno():
    try:
        return repo.comprasPorAlumno()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/agregados/alumnos-con-mas-de-un-pedido",
    response_model=list[AlumnoMasDeUnPedidoOut],
    status_code=200
)
def alumnos_con_mas_de_un_pedido():
    try:
        return repo.alumnosConMasDeUnPedido()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))