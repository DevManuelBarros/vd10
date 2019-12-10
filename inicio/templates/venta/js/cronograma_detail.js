<script type="text/javascript">
	function cambiarEstado()
	{
		 var pk = document.getElementById("id_unico").innerText;
		 var request = $.ajax({
		        type: "GET",
		        url: "{% url 'venta:cambiarValor' %}",
		        data : {"pk": pk,},
		    });	
		 request.done(function(response){
			    //alert(response.valor);
			 	$("#id_estado").text(response.valor);
		 });
	}
</script>