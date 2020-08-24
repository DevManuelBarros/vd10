from .lectorPDF import lectorPDF
from .lectorPDF import OrdenDeCompra
import re
from random import randrange

class lectorGigot:

    __pagina = 0
    __lineas_productos = []
    #Otros datos
    newObj = 0
    newObject = 0
    def __init__(self, ruta, num_cliente=3, cronograma=''):
        if cronograma=='':
            cronograma = 'C' + str(randrange(1000,9999)) + '-' + str(randrange(10,99))
        self.newObj = OrdenDeCompra()
        self.newObject = lectorPDF()
        self.newObject.cargarArchivo(ruta=ruta)
        self.__pagina = self.newObject.PDFALL
        patron_lineas =  re.compile(r'\d{4}X?\d{5}.{20,75}\d{4}\/\d{2}\/\d{4}.{20,30}')
        result = patron_lineas.findall(self.__pagina)
        #print(f'existeen {len(result)}, y los campos son:\n {result}')
        ###################################
        # Empezamos a trabajar la cabecera
        ##################################
        ## Fecha de Emision
        patron_emision = re.compile(r'Emisión:\s\d{2}\/\d{2}\/\d{4}')
        fecha_emision = patron_emision.search(self.__pagina)
        fecha_emision = self.__pagina[fecha_emision.start()+9:fecha_emision.end()].split('/')
        fecha_emision = str(fecha_emision[2] + '-' + fecha_emision[1] + '-' + fecha_emision[0])
        self.newObj.CabeceraOrdenDeCompra['fecha_emision'] = fecha_emision
        ## Referencia OC.
        patron_referencia = re.compile(r'Nro\.:\s\d{6}')
        referencia_oc = patron_referencia.search(self.__pagina).group().split(' ')[1]
        self.newObj.CabeceraOrdenDeCompra['referencia_oc'] = referencia_oc
        ## cliente
        self.newObj.CabeceraOrdenDeCompra['cliente'] = num_cliente
        ## campaña
        self.newObj.CabeceraOrdenDeCompra['campaña'] = cronograma
        ## definicion de circuito.
        if 'Entrega:CONSTITUCION 1667 - 22' in self.__pagina:
            self.newObj.CabeceraOrdenDeCompra['circuito'] = 'Consignacion'
        else:
            self.newObj.CabeceraOrdenDeCompra['circuito'] = 'Facturar'
        ## lineas
        self.newObj.CabeceraOrdenDeCompra['lineas'] = len(result)
        self.set_lineas(result)

    def set_lineas(self, lineas):
        '''
            Comenzamos la inclusión de lineas en la clase
            lectorPDF...
        '''
        for linea in lineas:
            ## Cargamos los codigos
            campos = linea.split(' ')
            campos = [r for r in campos if r != '']
            codigo = campos[0][4:]
            self.newObj.setCodigo(codigo)
            ##  Cargamos la descripción y fecha, uno y otro estan relacionados.
            fecha_entrega_patron = re.compile(r'\d{2}\/\d{2}\/\d{4}') #El final de la fecha es el comienzo de la descripcion
            fecha_entrega = fecha_entrega_patron.search(linea) #aquí obtenemos el número luego veremos como la trabajamos.
            descripcion = linea[fecha_entrega.end():].strip() #El final de fecha es el comienzo de la descripción.
            self.newObj.setDescripcion(descripcion)
            ##Cargamos la fecha.
            fecha_entrega = fecha_entrega.group().split('/')
            fecha_entrega = str(fecha_entrega[2] + '-' + fecha_entrega[1] + '-' + fecha_entrega[0])
            self.newObj.setFechaEntrega(fecha_entrega)
            self.newObj.setCantidad(campos[2])
            self.newObj.setPrecioUnit(campos[3])

    def get_registros(self):
        return self.newObj.getRegistros()
"""
o = lectorGigot(ruta='oc_gigot-8236.pdf')
print(o.get_registros())
"""
