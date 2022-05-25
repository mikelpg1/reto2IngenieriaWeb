let ampliar_informacion = document.getElementById("ampliar_boton")

if(ampliar_informacion){

    ampliar_informacion.addEventListener("click",function(){
        let informacion = document.getElementById("amp_info");
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

                ` );
        informacion.appendChild(texto);
        document.getElementById("ampliar_boton").style.visibility="hidden";
    })
}