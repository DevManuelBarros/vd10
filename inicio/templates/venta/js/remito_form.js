{% load static %}
<script src="{% static 'formset/jquery.formset.js' %}"></script>
<script type="text/javascript">
	//Formset Row.... cargamos la funcion
    $('.formset_row').formset({
        addText: 'Agregar Linea',
        deleteText: 'Eliminar',
        prefix: 'productolineasrm_set',
		instancia : 'remito'
    });
    
    //Cuando carga el documento incrustando las funciones en el documento.
	$(document).ready(function() {
        $("#id_cliente").on("change", getDatos);
        $("#confirm-data").on("click", getProductos);
        $("input[id^='id_productolineasrm_set-']").on("change", calcularTotal);
		$("input[id$='-total_unidades']").prop('disabled', true);
		$("#button-submit").prop("disabled", true);
        $("#comprobador-concordancia").on("click", autorizarRemito);	
    });
	
	
	//getDatos trae los datos de los clientes y lo agrega mediante ajax.
	//Esta asociado el evento: "change" en el select->#id_cliente
	function getDatos(valor) {
		// Obtenes el valor del cliente seleccionado.
        var clienteId = $("#id_cliente").val();
       //Comprobamos que la variable clienteId contenga algún valor.
        if (clienteId) {
			if(valor=='[object Object]'){
			// Eliminamos las opciones anteriores del select
			$("#id_ordencompra").html("");
					   }

			//Agregamos un llamado ajax.
			// el tipo es GET
			// la url según lo que se determina en la documentación
			// data: pasamos el valor del cliente.
		    var request = $.ajax({
                type: "GET",
                url: "{% url 'venta:get_datos' %}",
                data: {"id_cliente": clienteId,},
            });

		    //Luego de haber realizado la llamada mediante Ajax, 
		    //trabajamos con los valores devueltos.
            request.done(function(response) {
            // Agregamos los resultados al select
			if(valor=='[object Object]'){		
				$("#id_ordencompra").html(response.ordenesdecompra);
				$("#id_ordencompra").trigger("change", [false]);
				 
				}             
            							});
        	} else {
				if(valor=='[object Object]'){
            		$("#id_ordencompra").html("<option value='' selected='selected'>---------</option>");
            		$("#id_ordencompra").trigger("change", [false]);
											};
        		    }
			}

	

	function getProductos()
	{
		if(comprobarValoresCabecera()){
		if($(this).val()=='Confirmar Datos'){
		$('#cabecera').find('input, textarea, button, select').attr('disabled','disabled');
		//$("#cabecera").css('display','none');

		$("#second-form").css('visibility', 'visible');
		$(this).val("Modificar Cabecera");
		//$(this).tigger("onclick");
		getDatosProducts(0);
		}else{
			$("#cabecera").css('display', 'inline');
			$("#second-form").css('visibility', 'hidden');
			$(this).val("Confirmar Datos");
		};
		}
		
	}
	function calcularTotal()
	{
		array_datos = $(this).attr("id").split("-");
		cajas = $("input#" + array_datos[0] + "-" + array_datos[1] + "-cajas").val();
		cantidad = $("input#" + array_datos[0] + "-" + array_datos[1] + "-cantidad").val();
		$("input#" + array_datos[0] + "-" + array_datos[1] + "-total_unidades").val(cajas * cantidad);		
	}
	
	function comprobarValoresCabecera()
	{
		//alert($("select#id_cliente").val());
		if($('input#id_referencia_externa').val()=="")
		{
			alert("Debe indicar una referencia al remito");
			return false
		}
		if($("select#id_cliente").val()=="")
		{
			alert("Debe seleccionarse un cliente");
			return false
		}
		if($("select#id_ordencompra").val()=="")
		{
			alert("Debe seleccionarse una Orden de Compra");
			return false
		}
		if($('input#id_fecha_emision').val()=="")
		{
			alert("Debe indicarse una fecha");
			return false
		}
		return true
	}
	
	function autorizarRemito()
	{
		$("input[id$='-total_unidades']").prop('disabled', false);
		$("#cabecera").css('display', 'inline');
		$("#button-submit").prop("disabled", false);

	}
	
	 function getDatosProducts(valor) {
         var ordencompraId = $("#id_ordencompra").val();
         //alert(ordencompraId);
         if (ordencompraId) {
				if(valor=='[object Object]'){
					// Eliminamos las opciones anteriores del select
				$("select[id^='id_productolineasrm_set']").each(function(index){
				$(this).html("");
				});
				}
				else
				{
				$("select#id_productolineasrm_set-" + valor + "-producto").html("");
				}

			    var request = $.ajax({
                 type: "GET",
                 url: "{% url 'venta:get_productos' %}",
                 data: {
                     "id_ordencompra": ordencompraId,
                 },
             });

             request.done(function(response) {
                 // Agregamos los resultados al select
				if(valor=='[object Object]'){		
					$("select[id^='id_productolineasrm_set']").each(function(index){
						$(this).html(response.productos);
					 
					});
					 
					}else
					{
						//alert("select#id_productolineasoc_set-" + valor + "-producto");
					$("select#id_productolineasrm_set-" + valor + "-producto").html(response.productos);

					}
              
             });
         } else {
				if(valor=='[object Object]'){
};
         }
	}
	 
	 function controlarNumeracion()
	 {
		 //El id de Punto2 es 3.
		 if($(this).val() == 3)
		 {
			
			 var request = $.ajax({
                 type: "GET",
                 url: "{% url 'venta:get_numeracionRM' %}",
             });

             request.done(function(response) {
            	 $("#id_referencia_externa").val(response.next); 
             });			 
		 }else{
			 //Si no es el Punto2 Debe eliminar lo escrito
			 $("#id_referencia_externa").val("");
		 }
		 
	 }
</script>