from time import strftime, localtime

class colorines_html:
    __log = 0
    __nombre = ''
    # _type : [aparece entre [], color parentesis, color mensaje
    __dict_type ={
            'info'     : ['Inf', 'text-primary', 'text-warning', 'text-info font-italic'],
            'error'    : ['Err' , 'text-dark', 'text-danger', 'text-danger'],
            'agregar'  : [' + ' , 'text-info font-weight-bold', 'text-secondary', 'text-white'],
            'eliminar' : [' - ', 'text-danger', 'text-warning', 'text-warning'],
            'proceso'  : [' * ', 'text-info', 'text-primary', 'text-primary font-weight-bold'],
            'exito'    : [' ! ', 'text-success', 'text-warning font-weight-bold', 'text-success font-weight-bold']
            }
    
    # Limpiamos el log.
    def __init__(self, nombre_log='--Log Automatico--'):
        self.__log = []
        self.__nombre = nombre_log

    def intro(self, _type, _msg):
        '''
            Aqui guardamos el log, como un array, 
            luego podemos seleccionar como desplegarlo...
        '''
        _time = strftime('%H:%M:%S', localtime()) # aqui guarmamos la hora:minuto:segundo en que se genera el log.
        self.__log.append((self.__dict_type[_type.lower()], _msg, _time))

    def log2html(self):
        '''
            Esta función convierte el log cargado en formato Html.
        '''
        html = '<div style="background-color : black;"><code>' 
        html += '<h3 class="text-center">' + '-'* (len(self.__nombre) + 4 ) + '</h3><br>'
        html += f'<h3 class="text-success text-center">{self.__nombre}</h3><br>'
        html += '<h3 class="text-center">' + '-'* (len(self.__nombre)+ 4 ) + '</h3><br>'
        for type_log, _msg, _time in self.__log:
            html += f' <span class="text-info"> {_time}</span>-><span class="{type_log[1]}">[<span class="{type_log[2]}">{type_log[0]}</span>] </span>'
            html += f' <span class="{type_log[3]}">{_msg}</span><br>'
        html += '</code></div>'
        return html

    def log2Linux(self):
        '''
            Aqui permitira generar un log para mostrar en Linux.
        '''
        pass

    def log2Windows(self):
        '''
            Aqui permitira generar un log para mostrar en Windows
        '''
        pass
    

"""
log = colorines_html('Subiendo O.C')
log.intro_log('info', 'Esto es un mensaje')
log.intro_log('error', 'Este es un error')
log.intro_log('Eliminar', 'Se esta por eliminar este campo')
log.intro_log('Proceso', 'Este es un proceso...')
log.intro_log('Agregar', 'Creando un campo...')
print(log.log2html())
"""
