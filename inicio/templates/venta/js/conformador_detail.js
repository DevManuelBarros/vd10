<script type="text/javascript">
        $(document).ready(function(){
            $(".totalConf").on("click", getConformadorTotal);
            $("#totalComp").on("click", getTotalConf);
            $("#botonAjax").on("click", conformarRemito);
        });


        function getConformadorTotal(){
            var td = $(this).parents("tr").find("td")[3];
            var valor = td.textContent  || td.innerText;
            $(this).parents("tr").find("input").val(valor);
        }

        function getTotalConf(){
            var lista = $("#tablaPrincipal").find("tr");
            
            lista.each(function(index){
                if(index>0){
                    var td = $(this).find("td")[3];
                    var valor = td.textContent  || td.innerText;
                    $(this).find("input").val(valor);
                }
            });
        }


        function conformarRemito()
        {
                valor = crearCadenaAjax();
                var request = $.ajax({
                    type: "GET",
                    url: "{% url 'venta:conformarRemito' %}",
                    data : {"valor": valor},
                });	
             request.done(function(response){
                    alert(response.valor);
                    window.location.href = "{% url 'venta:RemitoListar' %}" ;
             });

        }

        function crearCadenaAjax()
        {
            var valor = "";
            valor += $("#td_remito_id").text() + "!";
            var lista = $("#tablaPrincipal").find("input");
            
            lista.each(function(index){
                valor += $(this).attr("id") + "=" + $(this).val() + "@";
               
            });
            return valor;
        }
</script>