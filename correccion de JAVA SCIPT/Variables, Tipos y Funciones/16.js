function esMayorYeison(davidEdad) {
if (davidEdad >= 18) {
return true;
} else {
return false;
}
}

function esMayorYeisonSimple(davidEdad) {
return davidEdad >= 18;
}

console.log("Edad 20:", esMayorYeison(20));
console.log("Edad 16:", esMayorYeison(16));

// TIP: Puedes simplificar condiciones booleanas retornando directamente la comparación.