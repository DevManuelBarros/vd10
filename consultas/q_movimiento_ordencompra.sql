SELECT * FROM venta_movimientos
INNER JOIN venta_productolineasoc
ON venta_productolineasoc.id = venta_movimientos.id_registro
INNER JOIN venta_ordencompra
ON venta_ordencompra.id = venta_productolineasoc.OrdenCompra_id
WHERE venta_movimientos.tipo_documento = 'orden_de_compra';