//Creo variable que es = al id del boton
var ampliar_informacion = document.getElementById("ampliar_boton")

//Si se ejecuta la variable
if(ampliar_informacion){
    // Registra el evento click a la variable
    ampliar_informacion.addEventListener("click",function(){
        
        //Variable que devuelve id nuevo
        let informacion = document.getElementById("amp_info");
        //Crea un nodo de texto
        let texto = document.createTextNode(
                `
                Para Deustronic Components S.L. la sostenibilidad no
                es un proyecto, sino una actitud y un camino hacia un futuro mejor. Los caminos hacia la 
                sostenibilidad son tan diversos como nuestros clientes y empleados...Por ello estamos comprometidos 
                con las personas, la sociedad y el medio ambiente. Para disfrutar de una vida mejor y llena de 
                oportunidades. Vayamos juntos a por el. Para implementar esta promesa de sostenibilidad 
                
                
                de una forma transparente, hemos creado la etiqueta Better Way, bajo la cual, agrupamos todo lo 
                relacionado con la sostenibilidad, la sociedad y la protección del medioambiente.Para Deustronic 
                Components S.L. la sostenibilidad no es un proyecto, sino una actitud y un camino hacia un futuro mejor. 
                
                
                Los caminos hacia la sostenibilidad son tan diversos como nuestros clientes y empleados...Por ello 
                estamos comprometidos con las personas, la sociedad y el medio ambiente. Para disfrutar de una vida
                mejor y llena de oportunidades. Vayamos juntos a por el. Para implementar esta promesa de 
                
                sostenibilidad de una forma transparente, hemos creado la etiqueta Better Way, bajo la cual, agrupamos 
                todo lo relacionado con la sostenibilidad, la sociedad y la protección del medioambiente

                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                aaaaaaaaaaaaaaaaaaaaaaaa

                ` 
        );
        //Agrega un nuevo nodo al final de la lista del elemento texto de un elemento padre (informacion)
        informacion.appendChild(texto);
    })
}