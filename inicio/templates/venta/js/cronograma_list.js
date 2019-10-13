<script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
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


function filtroNombre() {
	  var input, filter, table, tr, td, i, txtValue;
	  input = document.getElementById("filtroNombre");
	  filter = input.value.toUpperCase();
	  table = document.getElementById("tablaResultado");
	  tr = table.getElementsByTagName("tr");
	  for (i = 0; i < tr.length; i++) {
	    td = tr[i].getElementsByTagName("td")[0];
	    if (td) {
	      txtValue = td.textContent || td.innerText;
	      if (txtValue.toUpperCase().indexOf(filter) > -1) {
	        tr[i].style.display = "";
	      } else {
	        tr[i].style.display = "none";
	      }
	    }       
	  }
	}
	
function filtroCliente(){
	
}
</script>