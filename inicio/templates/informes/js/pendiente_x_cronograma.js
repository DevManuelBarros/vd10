<script type="text/javascript">
function filtros() 
	{
 
		  //definimos todas las variables
		  var input, filter, table, tr, td, i;
		  //levantamos los datos de codigo
		  input = document.getElementById("clientes");
		  filter = input.options[input.selectedIndex].value;

		 //tomamos todos los datos de la tabla
		 table = document.getElementById("tablaResultado");
		 tr = table.getElementsByTagName("tr");
		 for (i = 0; i < tr.length; i++) 
		 {
			 //Tomamos cada columna necesaria
			 td = tr[i].getElementsByTagName("td")[0];

			 
		    //alert(td + td2 + td3);
		    //Si de los dos campos obtenemos algo continua la comprabacion
		    if (td) 
		    {
		      //Obtenemos los valores segun corresponda.
		      txtValue  = td.textContent  || td.innerText;

		      			if (txtValue.toUpperCase().indexOf(filter) > -1)
		      			{
		      				tr[i].style.display = "";
				     	} 
				     	 else 
				     	{
				       		tr[i].style.display = "none";
				     	}
				     	break;
		
		    }     

		}
	}
</script>