var eventHandler = function(event) {
    event.preventDefault();
    precio = document.getElementById("id_precioTotal").value;
    cantidad = document.getElementById("id_cantidadproducto").value;
    if(precio <= 0){
        alert("El precio debe ser mayor que 0");
    }else if(cantidad <= 0){
        alert("La cantidad debe ser mayor que 0");
    }else{
        event.target.submit();
    }
}
var form = document.getElementsByClassName("acciones")[0];
form.addEventListener("submit", eventHandler);