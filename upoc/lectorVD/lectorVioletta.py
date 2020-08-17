
from .lectorPDF import lectorPDF
from .lectorPDF import OrdenDeCompra
import re

"""
Pasos:
1.Abrir
2.Juntamos todas los separadores
3.Creamos separador con "Número de artículo europeo" y lo almacenamos.
"""
class lectorVioletta:
    
    __pagina = ''

    #Otros datos
    newObj = 0
    newObject = 0
    def __init__(self, ruta):
        self.newObj = OrdenDeCompra()
        self.newObject = lectorPDF()
        self.newObject.cargarArchivo(ruta=ruta)
        self.__pagina = self.newObject.crearSeparador("Número de artículo europeo", almacenar=True)


    def procesarArchivo(self):
        resultado = []
        for lala in self.__pagina[0]:
            if lala.find("_") > 0:
                lala = lala[self.findLastChar(lala, "_"):]
                resultado.append(lala)
            else:
                resultado.append(lala)
        final = []
        for newSplit in resultado[:-1]:
            temp = newSplit.split("  ")
            result = []
            for nTemp in temp:
                if nTemp != '':
                    result.append(nTemp)
            final.append(result)

        #Fecha Entrega
        patron_fecha_entrega = re.compile(r'entrega\s\d{2}\.\d{2}\.\d{4}')
        fecha_entrega = str(patron_fecha_entrega.search(self.newObject.PDFALL).group()).replace('entrega ', '')
        fecha_entrega = fecha_entrega.replace('.','-')
        #self.newObj.CabeceraOrdenDeCompra['fecha_entrega'] = fecha_entrega
        for temp in final:
            self.newObj.setCodigo(temp[0])
            self.newObj.setDescripcion(temp[1])
            self.newObj.setCantidad(temp[2])
            self.newObj.setPrecioUnit(temp[4])
            self.newObj.setFechaEntrega(fecha_entrega)
        self.getHead()
        return self.newObj

    def getHead(self):
        texto = self.newObject.PDFALL
        
        #Campaña 01/2020
        patron_camp = re.compile(r'\d{2}/\d{4}')
        pCamp = patron_camp.search(texto)
        campana = texto[pCamp.start():pCamp.end()].replace('/','-')
        campana = 'C' + campana
        self.newObj.CabeceraOrdenDeCompra['campaña'] = campana
                #OrdenCompra.
        
        patron_orden_compra =  re.compile(r'\d{10}\/\d')
        arrayOC = str(patron_orden_compra.search(texto).group()).split('/')
        self.newObj.CabeceraOrdenDeCompra['referencia_oc'] = arrayOC[0]
        if arrayOC == '1':
            self.newObj.CabeceraOrdenDeCompra['circuito'] = 'Facturar'
        else:
            self.newObj.CabeceraOrdenDeCompra['circuito'] = 'Consignacion'
        #Fecha de Emision
        self.newObj.CabeceraOrdenDeCompra['cliente'] = 'Violetta'
        patron_fecha_emision = re.compile(r'\/ \d{2}\.\d{2}\.\d{4}')
        fecha_emision = str(patron_fecha_emision.search(texto).group()).replace('/ ', '')
        fecha_emision = fecha_emision.replace('.', '-')
        self.newObj.CabeceraOrdenDeCompra['fecha_emision'] = fecha_emision
    
    def fullText(self):
        return self.__fullText

    def findLastChar(self, cadena, caracter):
        numero = 0
        index = 1
        for cad in cadena:
            if(cad==caracter):
                numero = index
            index +=1
        return numero


