
<script type="text/javascript">
/***
Archivo: remito_form.js
Asociado : formito_form.html

Metodos y funciones contenidos:
getCreonograma();
get_today();
Asignaciones:
$('.formset_row').formset();
$(document).ready() 

***/

    $('.formset_row').formset({
        addText: 'Agregar Linea',
        deleteText: 'Eliminar',
        prefix: 'productolineasoc_set',
		instancia : 'ordencompra'
    });

	$(document).ready(function() {
			$(".signup-btn").modalForm({
				formURL: "{% url 'gral:ProductoCreatePartial' %}"
			});



            $("#id_cliente").on("change", getCronograma);
            //$(".col-md-4 mb-3").html("<a href='#' id='get_today'>Hoy</a>");
            
/*            $('.col-md-4 mb-3').each(function(indice, elemento) {
  					console.log(el	emento);
  					
				});*/
            
            $("#get_today").on("click", get_today);
            //Vaciamos los select que traen valores por defecto.
            $("select#id_productolineasoc_set-0-producto").html("<option value='' selected='selected'>---------</option>");
			//Esta Linea debería ejecutarse solo y solo si un formulario vacio.
			//$("#id_cronograma").html("<option value='' selected='selected'>---------</option>");
        });

	
	function getCronograma(valor) 
	{
            var clienteId = $("#id_cliente").val();
            if (clienteId) 
            {
				if(valor=='[object Object]')
				{
					$("#id_cronograma").html("");
					// Eliminamos las opciones anteriores del select
					$("select[id^='id_productolineasoc_set']").each(function(index)
					{
					$(this).html("");
					});
				}
				else
				{
					$("select#id_productolineasoc_set-" + valor + "-producto").html("");
				}

			var request = $.ajax(
				{
                    type: "GET",
                    url: "{% url 'venta:get_cronogramas' %}",
                    data: {"id_cliente": clienteId,},
                });

            request.done(function(response) {
                // Agregamos los resultados al select
				if(valor=='[object Object]')
				{		
					$("#id_cronograma").html(response.cronogramas);
					$("select[id^='id_productolineasoc_set']").each(function(index)
					{
						$(this).html(response.productos);
					});
					$("#id_cronograma").trigger("change", [false]); 
				}
				else
				{
					$("select#id_productolineasoc_set-" + valor + "-producto").html(response.productos);
				}
                });
            } 
            else 
            {
				if(valor=='[object Object]')
				{
                $("#id_cronograma").html("<option value='' selected='selected'>---------</option>");
                $("#id_cronograma").trigger("change", [false]);
				};
            }
	}

	 //Colocamos la fecha del día y la colocamos en fecha de emisión.
	 function get_today()
	 {
	 	var f = new Date();
		var today = f.getFullYear() + "-" + (f.getMonth() +1) + "-" + f.getDate();
		$("#id_fecha_emision").val(today);
	 }
		

</script>