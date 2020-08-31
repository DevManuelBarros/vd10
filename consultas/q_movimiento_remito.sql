SELECT * FROM venta_movimientos
INNER JOIN venta_productolineasrm
ON venta_productolineasrm.id = venta_movimientos.id_registro
INNER JOIN venta_remito
ON venta_remito.id = venta_productolineasrm.remito_id
WHERE venta_movimientos.tipo_documento = 'remito';