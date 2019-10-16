{% load static %}
<script src="{% static 'formset/jquery.formset.js' %}"></script>
<script type="text/javascript">
/***
Archivo: remito_form.js
Asociado : formito_form.html

Metodos y funciones contenidos:
getCreonograma();

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
            $("#id_cliente").on("change", getCronograma);
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


</script>