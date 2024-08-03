var s = "45e"
console.log(s)
console.log(typeof s)
console.log(Number.parseInt(s))

var nombre = prompt("Hola! Me complace avisarle que todo lo que ingrese a partir de ahora tiene carácter de declaración juarada. Empecemos!. Ingrese su nombre")
var apellido = prompt("Ahora ingrese su apellido")
var jugar = prompt("¿Está listo para jugar?")
var caminar = prompt("¿Está listo para caminar mucho mucho mucho? (recuerde que está bajo juramento)")
var num1 = parseInt(prompt("Escriba un número del 1 al 1000"))
var titulo = "<h1>Bienvenido al Juego Rema</h1>"


document.write(titulo)
document.write("<h2>¡¡¡ Hola ", nombre, " ", apellido, " !!! </h2> <h3>A continuación se muestran las preguntas que acaba de responder bajo declaración jurada</h3>")
document.write("<p>1) ¿Va a cocinarle a Regi todos los platos que quiera?<span>", jugar, "</span></p>")
document.write("<p>2) ¿Regi es la campeona de todos los juegos?<span>", jugar, "</span></p>")
document.write("<p>3) ¿Regi siempre tiene razón en todo?<span>", jugar, "</span></p>")
document.write("<p>4) ¿Regi es peleadora?<span>", caminar, "</span></p>")
document.write("<p>5) ¿Cuánto besos planea darle a Regi cuando la vea?<span>", num1 * num1, "</span></p>")


alert("Gracias!")
