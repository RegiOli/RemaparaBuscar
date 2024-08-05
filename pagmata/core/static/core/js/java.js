function promptSiNo(message) {
    let response;
    do {
        if (response !== undefined) {
            alert("Por favor, ingrese 'sí' o 'no'.");
        }
        response = prompt(message).toLowerCase();
    } while (response !== 'sí' && response !== 'no' && response !== 'si');
    return response;
}

function promptNumber(message, min, max) {
    let number;
    do {
        if (number !== undefined) {
            alert(`Por favor, ingrese un número entero entre ${min} y ${max}.`);
        }
        number = parseInt(prompt(message));
    } while (isNaN(number) || number < min || number > max);
    return number;
}

var nombre = prompt("Hola! Me complace avisarle que todo lo que ingrese a partir de ahora tiene carácter de declaración jurada. Empecemos!. Ingrese su nombre");
var apellido = prompt("Ahora ingrese su apellido");
var jugar = promptSiNo("¿Está listo para jugar?");
var caminar = promptSiNo("¿Está listo para caminar mucho mucho mucho? (recuerde que está bajo juramento)");
var num1 = promptNumber("Escriba un número del 1 al 1000", 1, 1000);
var titulo = "<h1>Bienvenido al Juego Rema</h1>";

document.write(titulo);
document.write("<h2>¡¡¡ Hola ", nombre, " ", apellido, " !!! </h2> <h3>A continuación se muestran las preguntas que acaba de responder bajo declaración jurada</h3>");
document.write("<p>1) ¿Va a cocinarle a Regi todos los platos que quiera?<span>", jugar, "</span></p>");
document.write("<p>2) ¿Regi es la campeona de todos los juegos?<span>", jugar, "</span></p>");
document.write("<p>3) ¿Regi siempre tiene razón en todo?<span>", jugar, "</span></p>");
document.write("<p>4) ¿Regi es peleadora?<span>", caminar, "</span></p>");
document.write("<p>5) ¿Cuántos besos planea darle a Regi cuando la vea?<span>", num1 * num1, "</span></p>");

alert("¡Gracias!");

// Enviar datos a Django
var data = {
    nombre: nombre,
    apellido: apellido,
    jugar: jugar,
    caminar: caminar,
    num1: num1
};

fetch('/guardar_respuestas/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': '{{ csrf_token }}'
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => console.log('Success:', data))
.catch(error => console.error('Error:', error));


