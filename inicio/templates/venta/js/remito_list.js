<script type="text/javascript">
$(document).ready(function()
	{
	    	var request=$.ajax(
	    	{
		        type : "GET",
		        url  : "{% url 'venta:get_clientes' %}",
	    	});
	    	
	    	request.done(function(response)
	    	{
	    	$("#clientes_select").html(response.clientes);
	    	});
	});

	
	function filtroNombreCliente() 
	{
		  //definimos todas las variables
		  var input, filter, table, tr, td, i, txtValue, input2, filter2, td2, txtValue2;
		  //levantamos los datos de nombre
		  input = document.getElementById("filtroNombre");
		  filter = input.value.toUpperCase();
		  //levantamos los datos del cliente
		  input2 = document.getElementById("clientes_select");
		  input2 = input2.options[input2.selectedIndex].text;
		  filter2 = input2.toUpperCase();
		  //levantamos los datos de estado del cronograma.
		  input3 = document.getElementById("filtroEstado");
		  input3 = input3.options[input3.selectedIndex].text;
		  filter3 = input3.toUpperCase();
		  //tomamos todos los datos de la tabla
		  table = document.getElementById("tablaResultado");
		  tr = table.getElementsByTagName("tr");
		 
		
		      
		      
		
		 
		  //recorremos toda la tabla
		 for (i = 0; i < tr.length; i++) 
		 {
			 //Tomamos cada columna necesaria
			 td = tr[i].getElementsByTagName("td")[0];
			 td2 = tr[i].getElementsByTagName("td")[3];
			 td3 = tr[i].getElementsByTagName("td")[4];
			 
		    
		    //Si de los dos campos obtenemos algo continua la comprabacion
		    if (td && td2 && td3) 
		    {
		      //Obtenemos los valores segun corresponda.
		      txtValue  = td.textContent  || td.innerText;
		      txtValue2 = td2.textContent || td2.innerText;
		      txtValue3 = td3.textContent || td3.innerText;
		      

		      if(txtValue3.toUpperCase().indexOf('FALSE') > -1)
		      {

		        txtValue3 = 'SIN';
		      }
		      else
		      {
		      	txtValue3 = 'CONFORMADO';
		      }
		      //Sumamos las condiciones para ver que tipo de filtro tenemos:
		      // filtro3 = 3 filtro2 = 2.
		      // A partir de esos valores sumamos: 
		      // si condicional es 0 = filtro1
		      // si condicional es 2 = filtro1 y filtro2
		      // si condicional es 3 = filtro1 y filtro3
		      // si condicional es 5 = filtro1 filtro2 y filtro3
		      var condicional = filter3 != 'TODOS' ? 3 : 0;
		      condicional += filter2 == '---------' ? 0 : 2;
		      
		      switch (condicional) 
		      {
		      		case 0:
		      			if (txtValue.toUpperCase().indexOf(filter) > -1)
		      			{
		      				tr[i].style.display = "";
				     	} 
				     	 else 
				     	{
				       		tr[i].style.display = "none";
				     	}
				     	break;
				    case 2:
				    	if (txtValue.toUpperCase().indexOf(filter) > -1 && txtValue2.toUpperCase().indexOf(filter2) > -1 ) 
				      	{
				        	tr[i].style.display = "";
				      	} 
				      	else {
				        	tr[i].style.display = "none";
				      	}
				      	break;
				    case 3:
				    	if (txtValue.toUpperCase().indexOf(filter) > -1 && txtValue3.toUpperCase().indexOf(filter3) > -1 ) 
				      	{
				        	tr[i].style.display = "";
				      	} 
				      	else {
				        	tr[i].style.display = "none";
				      	}
				      	break;
				    case 5:
				   		 if (txtValue.toUpperCase().indexOf(filter) > -1 && txtValue2.toUpperCase().indexOf(filter2) > -1 && txtValue3.toUpperCase().indexOf(filter3) > -1 ) 
				      	{
				        	tr[i].style.display = "";
				      	} 
				      	else {
				        	tr[i].style.display = "none";
				      	}
		      }
		    }     

		}
	}

</script>