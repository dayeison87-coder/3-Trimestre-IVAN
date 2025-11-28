// ejercicio09.js
function sumarArreglo(arr) {
 let yeison_moreno1 = 0;
 for (let yeison_moreno2 = 0; yeison_moreno2 < arr.length; yeison_moreno2++) {
 yeison_moreno1 += arr[yeison_moreno2];
 }
 return yeison_moreno1;
}
let ventas = [100, 200, 300, 400, 500];
console.log("Total:", sumarArreglo(ventas));
// Salida: 1500


//Anatomía del Bucle for
//Inicialización: let yeison_moreno2 = 0
// Comienza en el índice 0
//Condición: yeison_moreno2 < arr.length
//Continúa mientras yeison_moreno2 sea menor que la longitud
//Incremento: yeison_moreno2++
//Aumenta yeison_moreno2 después de cada iteración
//Acumulador: yeison_moreno1 += arr[yeison_moreno2]
//Va sumando cada elemento