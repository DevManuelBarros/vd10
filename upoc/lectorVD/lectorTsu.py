from .lectorPDF import lectorPDF
from .lectorPDF import OrdenDeCompra
import re


class lectorTsu:

    __pagina = 0
    __lineas_productos = []
    #Otros datos
    newObj = 0
    newObject = 0
    def __init__(self, ruta):
        self.newObj = OrdenDeCompra()
        self.newObject = lectorPDF()
        self.newObject.cargarArchivo(ruta=ruta)
        #self.__pagina = self.newObject.crearSeparador("Número de artículo europeo", almacenar=True)
        self.__pagina = self.newObject.PDFALL.split('CONDICIONES GENERALESLAS CONDI')[0]
        #patron = re.compile('\d{5}-\d.{2,35}\d{2},\d{4}.{1,12}\d{2}\/\d{2}\/d{4}')
        patron = re.compile(r'\d{5}-\d{1}.{4,30}\d{1,8}?\d{2}\.\d{4}.{2,8}\.\d{2}\d{2}\/\d{2}\/\d{4}')
        self.__lineas_productos = patron.findall(self.__pagina)
        for i, value in enumerate(self.__lineas_productos):
            self.__lineas_productos[i] = value.replace(',', '')
            # en versiones viejas hay problemas de separación de espacio vacios entre los 
            # números con esto lo resolvemos.
            patron_busqueda = re.compile(r'\d\s\d')
            grupos = patron_busqueda.findall(self.__lineas_productos[i])
            for item in grupos:
                new_value= item.replace(' ', '')
                self.__lineas_productos[i] = self.__lineas_productos[i].replace(item,new_value)
        # obtenemos orden de compra
        patron = re.compile(r'\d{6}\s{3,4}\d{1,2}')
        ordencompra = patron.search(self.__pagina).group()
        ordencompra, version = self.separar_orden_compra(ordencompra) 
        if int(version) > 1:
            self.newObj.CabeceraOrdenDeCompra['actualizar'] = 1
            self.newObj.CabeceraOrdenDeCompra['version'] = version
        self.newObj.CabeceraOrdenDeCompra['referencia_oc'] = ordencompra
        # fecha emision.
        patron = re.compile(r'\d{8}')
        fecha_emision = patron.search(self.__pagina).group()
        fecha_emision = fecha_emision[0:2] + '-' + fecha_emision[2:4] + '-' + fecha_emision[4:]
        circuito = 'Facturar'
        # obtenemos la campaña
        patron = re.compile(r'\d{4}-\d{2}')
        campana = patron.search(self.__pagina).group()
        fecha_anio, campana = campana.split('-')
        campana = 'C' + campana + '-' + fecha_anio
        self.newObj.CabeceraOrdenDeCompra['campaña'] = campana
        self.newObj.CabeceraOrdenDeCompra['fecha_emision'] = fecha_emision
        self.newObj.CabeceraOrdenDeCompra['circuito'] = 'Facturar'
        self.newObj.CabeceraOrdenDeCompra['cliente'] = 'Tsu'
        self.obtenerLineas()
        #print(self.newObj.getRegistros())

    def get_registros(self):
        return self.newObj.getRegistros()
        
    def separar_orden_compra(self, ordencompra):
        separado = ordencompra.split(' ')
        return separado[0], separado[-1]


    def obtenerLineas(self):
        patron = re.compile(r'\d{5}-\d{1}')
        patron_fecha = re.compile(r'\d{2}\/\d{2}\/\d{4}')
        codigos = patron.findall(self.__pagina)
        for item in codigos:
            self.newObj.setCodigo(item)
        patron = re.compile(r'\d{2,10}\.\d{5}')
        for linea in self.__lineas_productos:
            precio_unit = patron.search(linea)
            precio = precio_unit.group()[:-1]
            fecha = patron_fecha.search(linea) 
            monto_total = self.convertir_a_float(linea[precio_unit.end()-1:fecha.start()])
            cantidad, precio_unitario, cad_descripcion = self.logicNumber(precio, monto_total)
            #print(cantidad, precio_unitario, cad_descripcion)
            self.newObj.setFechaEntrega(fecha.group())
            self.newObj.setCantidad(cantidad)
            self.newObj.setPrecioUnit(precio_unitario)
            fin_descripcion = precio.replace(cad_descripcion, '',  1)
            fin = linea.index(str(fin_descripcion))
            descripcion = linea[7:fin] 
            self.newObj.setDescripcion(descripcion)





    def logicNumber(self,cadena_completa, total):
        ''' Encuentra la secuencia de números que corresponden a la linea d eproductos
            y devuelve los caracteres que pertenecen a la descripcion que permite darle el final
        '''
        inicio, resto = cadena_completa.split('.')   # la cadena viene con el formato \d{2,8}?.\d{4}
        inicio = str(inicio) # lo convertimos a str para trabajarlo
        for i in range(len(inicio), 0, -1): # comenzamos a recorrerlo de forma inversa
            numero_prueba = float(inicio[i:] + '.' + resto) # extraemos los números para comenzar a realizar las pruebas-
            a_buscar = int(round(total / numero_prueba,0)) # comprobamos si este número de prueba dar el resultado que buscamos.
            #print(f'total: {total} / precio hipotetico: {numero_prueba} = {a_buscar}')
            if str(a_buscar) in inicio[:i]:       # si entra aquí la división es correcta por lo que podemos concluir que la extración 
                min_descrip = inicio.split(str(a_buscar))[0] # es correcta... guardamos si quedo una parte de la descripción, esto agilizara 
                return a_buscar, numero_prueba, min_descrip # la busqueda y división en la cadena.
        return 0,0,'Error' # Si esta retornando acá claramente hay un error en todo el proceso.


    def convertir_a_float(self, texto):
        texto = texto.replace(' ', '')
        texto = texto.replace(',', '')
        return float(texto)


