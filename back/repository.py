import mysql.connector
from db import obtenerConexion


class RepoCafeteria:

    def conectarDB(self) -> mysql.connector.MySQLConnection:
        return obtenerConexion()

    # =========================================================
    # 3) CONSULTAS AVANZADAS (MULTITABLA)
    # 2 JOIN + 1 SUBCONSULTA + 1 IN
    # =========================================================

    def pedidosConAlumno(self):
        """
        JOIN: Pedido incluyendo el nombre del alumno
        """
        conx: mysql.connector.MySQLConnection = self.conectarDB()
        cursor = conx.cursor(dictionary=True)
        sql = """
            SELECT a.nombre, p.fecha, p.id_pedido, p.total
            FROM Alumno a
            JOIN Pedido p ON a.id_alumno = p.id_alumno;
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conx.close()
        return res

    def productosVendidosPorPedido(self):
        """
        JOIN: Productos vendidos y pedido en el que aparecen (con cantidad)
        """
        conx: mysql.connector.MySQLConnection = self.conectarDB()
        
        cursor = conx.cursor(dictionary=True)
        sql = """
            SELECT pp.id_pedido, pr.id_producto, pr.nombre AS producto, pp.cantidad
            FROM Pedido_Producto pp
            JOIN Producto pr ON pp.id_producto = pr.id_producto
            ORDER BY pp.id_pedido, pr.nombre;
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conx.close()
        return res

    def productosMayorAlPromedio(self):
        """
        SUBCONSULTA: Productos con precio mayor al promedio
        """
        conx: mysql.connector.MySQLConnection = self.conectarDB()
        cursor = conx.cursor(dictionary=True)
        sql = """
            SELECT nombre, precio
            FROM Producto
            WHERE precio > (SELECT AVG(precio) FROM Producto)
            ORDER BY precio DESC;
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conx.close()
        return res

    def alumnosQueHanRealizadoPedido(self):
        """
        IN: Alumnos que han realizado un pedido (sin duplicados)
        """
        conx: mysql.connector.MySQLConnection = self.conectarDB()
        cursor = conx.cursor(dictionary=True)
        sql = """
            SELECT nombre
            FROM Alumno
            WHERE id_alumno IN (
                SELECT DISTINCT id_alumno
                FROM Pedido
            )
            ORDER BY nombre;
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conx.close()
        return res

    # =========================================================
    # 4) AGREGADOS Y AGRUPACIÓN
    # COUNT, SUM, AVG/MAX/MIN, GROUP BY, HAVING (mínimo 5)
    # =========================================================

    def countPedidos(self):
        """
        COUNT: número de pedidos
        """
        conx: mysql.connector.MySQLConnection = self.conectarDB()
        cursor = conx.cursor(dictionary=True)
        sql = "SELECT COUNT(*) AS numero_de_pedidos FROM Pedido;"
        cursor.execute(sql)
        res = cursor.fetchone()
        cursor.close()
        conx.close()
        return res

    def sumTotalIngresos(self):
        """
        SUM: total de ingresos (suma de totales)
        """
        conx: mysql.connector.MySQLConnection = self.conectarDB()
        cursor = conx.cursor(dictionary=True)
        sql = "SELECT SUM(total) AS total_ingresos FROM Pedido;"
        cursor.execute(sql)
        res = cursor.fetchone()
        cursor.close()
        conx.close()
        return res

    def statsPreciosProducto(self):
        """
        AVG / MAX / MIN: promedio, más caro, más barato
        """
        conx: mysql.connector.MySQLConnection = self.conectarDB()
        cursor = conx.cursor(dictionary=True)
        sql = """
            SELECT
                AVG(precio) AS promedio,
                MAX(precio) AS mas_caro,
                MIN(precio) AS mas_barato
            FROM Producto;
        """
        cursor.execute(sql)
        res = cursor.fetchone()
        cursor.close()
        conx.close()
        return res

    def comprasPorAlumno(self):
        """
        GROUP BY: compras realizadas de cada alumno (count de pedidos)
        """
        conx: mysql.connector.MySQLConnection = self.conectarDB()
        cursor = conx.cursor(dictionary=True)
        sql = """
            SELECT p.id_alumno,a.nombre, 
            COUNT(p.id_pedido) AS compras_realizadas 
            FROM Pedido as p JOIN alumno AS a ON p.id_alumno = a.id_alumno 
            GROUP BY p.id_alumno;
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conx.close()
        return res

    def alumnosConMasDeUnPedido(self):
        """
        HAVING: alumnos con más de un pedido
        (en tu texto decías >1; si tu profe pide >2, cambia el número)
        """
        conx: mysql.connector.MySQLConnection = self.conectarDB()
        cursor = conx.cursor(dictionary=True)
        sql = """
            SELECT id_alumno, COUNT(id_pedido) AS pedidos
            FROM Pedido
            GROUP BY id_alumno
            HAVING pedidos > 1;
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        conx.close()
        return res