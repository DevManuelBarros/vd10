<script type="text/javascript">
$(document).ready(function(){
    var request = $.ajax({
        type: "GET",
        url: "{% url 'venta:get_clientes' %}",
    });
    
    request.done(function(response){
    	$("#clientes_select").html(response.clientes);
    });
	
});


function filtroNombreCliente() {
	  //definimos todas las variables
	  var input, filter, table, tr, td, i, txtValue, input2, filter2, td2, txtValue2;
	  //levantamos los datos de nombre
	  input = document.getElementById("filtroNombre");
	  filter = input.value.toUpperCase();
	  //levantamos los datos del cliente
	  input2 = document.getElementById("clientes_select");
	  input2 = input2.options[input2.selectedIndex].text;
	  filter2 = input2.toUpperCase();
	  //tomamos todos los datos de la tabla
	  table = document.getElementById("tablaResultado");
	  tr = table.getElementsByTagName("tr");
	  //recorremos toda la tabla
	  for (i = 0; i < tr.length; i++) {
	    //Tomamos cada columna necesaria
		td = tr[i].getElementsByTagName("td")[0];
	    td2 = tr[i].getElementsByTagName("td")[2];
	    //Si de los dos campos obtenemos algo continua la comprabacion
	    if (td && td2) {
	      //Obtenemos los valores segun corresponda.
	      txtValue = td.textContent || td.innerText;
	      txtValue2 = td2.textContent || td2.innerText;
	      //Si el select contiene valores vacios solo se filtra por el TextBox
	      if (filter2 == '---------') {
	    	  if (txtValue.toUpperCase().indexOf(filter) > -1){
	    		  tr[i].style.display = "";
		      } else {
		        tr[i].style.display = "none";
		      }

	      }else{
	    	      // En caso contrario filtramos por los dos valores.
			      if (txtValue.toUpperCase().indexOf(filter) > -1 && txtValue2.toUpperCase().indexOf(filter2) > -1) {
			        tr[i].style.display = "";
			      } else {
			        tr[i].style.display = "none";
			      }
	      }
	    }       
	  }
	}

</script>