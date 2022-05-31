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
                relacionado con la sostenibilidad, la sociedad y la protección del medioambiente.
                En los últimos años, gracias a diferentes campañas de concienciación, hemos conseguido cambiar nuestros 
                hábitos de consumo, haciéndolos más responsables y sostenibles. Ya son muchos los hogares que contribuyen 
                activamente a la separación de basura y cada día somos más conscientes de que esta práctica es el único modo 
                que tenemos para preservar y, por lo tanto, de disfrutar de nuestro planeta. El reciclaje funciona en cadena y 
                por ello, el simple hecho de tirar nuestra basura en un contenedor u otro es básico para poder disfrutar de los 
                beneficios energéticos obtenidos en el proceso de reciclaje y hacernos sertirnos mejor al saber que la reutilización 
                de una tonelada de papel salva la vida de 17 árboles.
                
                ` 
        );
        //Agrega un nuevo nodo al final de la lista del elemento texto de un elemento padre (informacion)
        informacion.appendChild(texto);
        document.getElementById('ampliar_boton').style.visibility='hidden';
    })
}