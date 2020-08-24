import os
from PyPDF2 import PdfFileReader

    



class lectorPDF:
    PDFText = 0
    PDFALL = 0
    tmpBufferLineas = 0
    Ruta = 0

    def cargarPaginas(self):
        for inx in self.PDFText:
            self.PDFALL += inx

    def __init__(self):
        self.PDFText = []
        self.PDFALL = ""
        self.tmpBufferLineas = []
        self.Ruta = ""

    def cargarArchivo(self, ruta):
        self.Ruta = ruta
        with open(ruta, 'rb') as f:
            archivoPDF = PdfFileReader(f)
            for pagina in range(archivoPDF.getNumPages()):
                self.PDFText.append(archivoPDF.getPage(pagina).extractText())
        self.cargarPaginas()


    def cantPaginas(self):
        return "La cantidad de paginas del documento es: {}".format(len(self.PDFText))

    def rutaActual(self):
        return "La ruta del actual documento es: {}".format(self.Ruta)
    
    def imprimirPagina(self, numPagina):
        if numPagina <= (len(self.PDFText) +1):
            return self.PDFText[numPagina - 1]
        else:
            return "Error: Fuera del indice." 

    def crearSeparador(self, separador, pagina="Todas", almacenar=False):
        resultado = []
        if pagina == "Todas":
            resultado.append(self.PDFALL.split(separador))
        else:
            resultado = self.PDFText[pagina - 1].split(separador)
            return resultado
        if almacenar==True:
            self.tmpBufferLineas = resultado
        return resultado


class OrdenDeCompra:    
    __codigo = 0
    __descripcion = 0
    __cantidad = 0
    __precio_unitario = 0
    __fecha_entrega = 0


    CabeceraOrdenDeCompra = {}

    def __init__(self):
        self.CabeceraOrdenDeCompra = {
        'fecha_emision' : '',
        'referencia_oc'    : '',
        'cliente'       : '',
        'campaña'       : '',
        'circuito'      : '',
        'lineas'        : 0 ,
        'actualizar'    : 0 ,
        'version'       : 1
        }
        self.__codigo = []
        self.__descripcion = []
        self.__cantidad = []
        self.__precio_unitario = []
        self.__fecha_entrega = []

    def setCodigo(self, codigo_completo):
        if ' ' in codigo_completo: 
            codigo_completo  = codigo_completo.split(" ")[1]
        self.__codigo.append(codigo_completo)

    def setDescripcion(self, descripcion):
        descripcion = descripcion.strip()
        self.__descripcion.append(descripcion)

    def setCantidad(self, cantidad):
        if not isinstance(cantidad, int):
            if ',' in cantidad:
                cantidad = cantidad.split(',')[0]
            cantidad = cantidad.replace(".", "")
            int_cantidad = int(cantidad)
            self.__cantidad.append(int_cantidad)
        else:
            self.__cantidad.append(cantidad)
    
    def setPrecioUnit(self, precio_unitario):
        if isinstance(precio_unitario, str):
            precio_unitario = precio_unitario.replace(",", ".")
            self.__precio_unitario.append(float(precio_unitario))
        if isinstance(precio_unitario, float):
            self.__precio_unitario.append(precio_unitario)

    def setFechaEntrega(self, fecha_entrega):
        if '/' in fecha_entrega:
            fecha_sep  = fecha_entrega.split('/')
            fecha_entrega = fecha_sep[2] + '-' + fecha_sep[1] + '-'  +fecha_sep[0]
        self.__fecha_entrega.append(fecha_entrega)


    def getRegistros(self):
        tmpDict = {}
        self.CabeceraOrdenDeCompra['lineas'] = len(self.__codigo)
        tmpDict['cabecera'] = self.CabeceraOrdenDeCompra
        for index, codigo in enumerate(self.__codigo):
            tmp = {}
            tmp['codigo'] = codigo
            tmp['descripcion'] = self.__descripcion[index]
            tmp['cantidad'] = self.__cantidad[index]
            tmp['precio_unitario'] = self.__precio_unitario[index]
            tmp['fecha_entrega'] = self.__fecha_entrega[index]
            tmpDict[index] = tmp 
        return tmpDict


