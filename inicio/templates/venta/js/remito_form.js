{% load static %}
<script src="{% static 'formset/jquery.formset.js' %}"></script>
<script type="text/javascript">
/***
Archivo: remito_form.js
Asociado : formito_form.html

Metodos y funciones contenidos:

function getDatos(valor);
function getProductos();
function calcularTotal()
function comprobarValoresCabecera();
function obtenerNumeroRegistros();
function restablecerValores();
function getDatosProducts(valor);
function controlarNumeracion();

Asignaciones:
$('.formset_row').formset();
$(document).ready() 

***/
	//variables Globales:

	prefix_global = 'productolineasrm_set';

	//Formset Row.... cargamos la función que permitira agregar lineas
	//del formulario hijo al formulario principal.
    $('.formset_row').formset(
    {
        addText: 'Agregar Linea', //Texto que aparece en el formulario para agregar Linea.
        deleteText: 'Eliminar',   //Texto que aparece en el formulario para Eliminar Linea.
        prefix: prefix_global, //Se pasa el prefijo que se utilizara en el formset y que tiene 
        								//relizacion con el formulario.
		instancia : 'remito'			//instacia es un atributo personalizado, donde podemos indicar
										//un valor para luego tener diferentes comportamientos.
    });
    
    //Cuando carga el documento incrustando las funciones en el documento.
	$(document).ready(function() 
	{
		//id_productolineasrm_set-0-remito
		alert(prefix_global);
		//$("select[id$='-producto']").on("change", function(){alert('asd')});
        $("#id_cliente").on("change", getDatos);
        $("#confirm-data").on("click", getProductos);
        $("input[id^='id_" + prefix_global + "-']").on("change", calcularTotal);
		$("input[id$='-total_unidades']").prop('readonly', 'readonly');
		$("input[id$='-pendientes']").prop('readonly', 'readonly');
		$("#button-submit").on("click", actDatos);
		$("#get_today").on("click", get_today);
		$("#id_tipo_documento").on("change",controlarNumeracion);
		vaciarSelectOC();
    });
	
	
	//getDatos trae los datos de los clientes y lo agrega mediante ajax.
	//Esta asociado el evento: "change" en el select->#id_cliente
	function getDatos(valor) 
	{
		// Obtenes el valor del cliente seleccionado.
		var clienteId = $("#id_cliente").val();
		var circuito = $("#id_tipo_documento").val();
		//Comprobamos que la variable clienteId contenga algún valor.
		if (clienteId) 
		{
			if(valor=='[object Object]')
			{
				// Eliminamos las opciones anteriores del select
				$("#id_ordencompra").html("");
			}
			//Agregamos un llamado ajax.
			// el tipo es GET
			// la url según lo que se determina en la documentación
			// data: pasamos el valor del cliente.
			var request = $.ajax(
			{
				type: "GET",
				url: "{% url 'venta:get_datos' %}",
				data: {"id_cliente": clienteId,'circuito': circuito},
			});

			//Luego de haber realizado la llamada mediante Ajax, 
			//trabajamos con los valores devueltos.
			request.done(function(response) 
			{
				// Agregamos los resultados al select
				if(valor=='[object Object]')
				{		
					$("#id_ordencompra").html(response.ordenesdecompra);
					$("#id_ordencompra").trigger("change", [false]);
				}             
			});
		}
			else
			{
				if(valor=='[object Object]')
				{
					vaciarSelectOC();
				}
			}		
		}

		//Cargar por defecto la selección del option y dejarlo limpio, esto se puede usar al principio
		//de la carga del formulario y cuando 
		function vaciarSelectOC()
		{
				$("#id_ordencompra").html("<option value='' selected='selected'>---------</option>");
				$("#id_ordencompra").trigger("change", [false]);
		}


		// Trae información de los productos seleccionados y bloquea la cabecera.
		function getProductos()
		{
			if(comprobarValoresCabecera())
			{
				if($(this).val()=='Confirmar Datos')
				{
					$('#cabecera').find('input, textarea, button, select').prop('disabled',true);
					$("#second-form").css('visibility', 'visible');
					$(this).val("Modificar Cabecera");
					getDatosProducts(0);
			}
				else
			{
					$('#cabecera').find('input, textarea, button, select').prop('disabled',false);
					$("#second-form").css('visibility', 'hidden');
					$(this).val("Confirmar Datos");
			};
			}	
	}

	//Se calcula automaticamente el total y lo va mostrando en el formulario.
	// esta asinado como evento al input asinado como id: "input[id^='id_productolineasrm_set-']"
	function calcularTotal()
	{
		//primero separamos el id, para obtener cual es el número de registro sobre el que
		//estamos trabajando.
		array_datos = $(this).attr("id").split("-");
		//[0]: productolineasetrm_set [1]: 1(número de registro) -cajas, con esto obtenemos
		cajas = $("input#" + array_datos[0] + "-" + array_datos[1] + "-cajas").val();
		//igual que el anterior pero obtenemos la cantidad x cajas
		cantidad = $("input#" + array_datos[0] + "-" + array_datos[1] + "-cantidad").val();
		//Accedemos al -totalunidades y obtenemos el producto de las cajas por las cantidad.
		$("input#" + array_datos[0] + "-" + array_datos[1] + "-total_unidades").val(cajas * cantidad);		
	}
	
	//Comprobamos si la cabecera contiene errores
	function comprobarValoresCabecera()
	{
		//Si no tiene una referencia.
		if($('input#id_referencia_externa').val()=="")
		{
			alert("Debe indicar una referencia al remito");
			return false
		}
		//Si no hay seleccionado un cliente
		if($("select#id_cliente").val()=="")
		{
			alert("Debe seleccionarse un cliente");
			return false
		}
		//Si no hay una orden de compra asociada.
		if($("select#id_ordencompra").val()=="")
		{
			alert("Debe seleccionarse una Orden de Compra");
			return false
		}
		//Si no hay una fecha.
		if($('input#id_fecha_emision').val()=="")
		{
			alert("Debe indicarse una fecha");
			return false
		}
		//Si ningunas de las condiciones anteriores salta devuelve true.
		return true
	}
	
	//Obtenemos cuantos registros tenemos actualmente en el 
	//formulario. Sirve para realizar comprobaciones.
	function obtenerNumeroRegistros()
	{
		valor = $(".delete-row").length;
		return  valor - 1
	}

	//Restablece los valores de los campos input cuando 
	//corresponda.
	function restablecerValores()
	{
		registros = obtenerNumeroRegistros();
		for(i=0; i <= registros; i++)
		{
			$("input#id_" + prefix_global +"-" + i + "-cajas").each(function(index)
			{
						$(this).val("");
			});
			$("input#id_" + prefix_global + "-" + i + "-cantidad").each(function(index)
			{
						$(this).val("");
			});
			$("input#id_" + prefix_global + "-" + i + "-total_unidades").each(function(index)
			{
						$(this).val("");
			});
		}
	}

	function getDatosProducts(valor) 
	{		
		var ordencompraId = $("#id_ordencompra").val();
		// Comprobamos que contenga algún valor.
		if (ordencompraId)	
		{
			if(valor==obtenerNumeroRegistros())
			{
				$("select#id_" + prefix_global + "-" + valor + "-producto").html("");
			}
			else
			{
				$("select[id^='id_" + prefix_global + "']").each(function(index)
				{
					$(this).html("");
				});
			}
		//creamos la llamada ajax.
		var request = $.ajax({
								type: "GET",
								url: "{% url 'venta:get_productos' %}",
								data: {"id_ordencompra": ordencompraId,},
							});
			//Cuando obtenemos la respuesta comenzamos con la carga de valores.
			request.done(function(response) 
			{
				if(valor==obtenerNumeroRegistros())
				{
					$("select#id_" + prefix_global + "-" + valor + "-producto").html(response.productos);
					if(valor==0)
					{
						restablecerValores();
					}
				}
				else
				{
					$("select[id^='id_" + prefix_global + "']").each(function(index)
					{

						$(this).html(response.productos);
					});
					restablecerValores();
				}
			});
		}
		
	}
	
	//Función para activar los datos y poder guardarlos correctamente.
	function actDatos()
	{
		$('#cabecera').find('input, textarea, button, select').prop('disabled',false);
	}


	//Númeración automatica de la orden de traslado.
	function controlarNumeracion()
	 {
		 
		 if($(this).val() == 'OrdenTraslado')
		 {
			
			 var request = $.ajax(
			 {
                 type: "GET",
                 url: "{% url 'venta:get_numeracionRM' %}",
             });
             
             request.done(function(response) 
             {
            	 $("#id_referencia_externa").val(response.next);
            	 $("#id_referencia_externa").prop("readonly", "readonly");
             });			 
		 	}
		 	else
		 	{
				 //Si no es el Punto2 Debe eliminar lo escrito
				 $("#id_referencia_externa").val("");
				 $("#id_referencia_externa").prop("readonly", false);
		 	}
		 vaciarSelectOC();
	 }

	 //Colocamos la fecha del día y la colocamos en fecha de emisión.
	 function get_today()
	 {
	 	var f = new Date();
		var today = f.getFullYear() + "-" + (f.getMonth() +1) + "-" + f.getDate();
		$("#id_fecha_emision").val(today);
	 }
</script>