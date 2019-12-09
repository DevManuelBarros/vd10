<script type="text/javascript">
        $(document).ready(function(){
            $(".totalConf").on("click", getConformadorTotal);
            $("#totalComp").on("click", getTotalConf)
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

</script>