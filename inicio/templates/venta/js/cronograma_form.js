<script type="text/javascript">
		$(document).ready(function()
		{
			siExisteFecha();
		});
		
		function invertirFecha(array)
		{
			return array[2] + "-" + array[1] + "-" + array[0];
		}
		
		function siExisteFecha()
		{
			//alert($("#id_fecha_inicio").attr('value'));
			if($("#id_fecha_inicio").attr('value'))
			{
				var fecha = invertirFecha($("#id_fecha_inicio").attr('value').split("/")); 
				$("#id_fecha_inicio").val(fecha);
			}
			if($("#id_ficha_finalizacion"))
			{
				var fecha = invertirFecha($("#id_fecha_finalizacion").attr('value').split("/")); 
				$("#id_fecha_finalizacion").val(fecha);
			}
		}
</script>