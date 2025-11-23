function clasificarYeison(davidF) {
if (davidF >= 14 && davidF < 32) {
return "Temperatura baja";
} else if (davidF >= 32 && davidF < 68) {
return "Temperatura adecuada";
} else if (davidF >= 68 && davidF < 96) {
return "Temperatura alta";
} else {
return "Temperatura desconocida";
}
}

console.log(clasificarYeison(25));
console.log(clasificarYeison(50));
console.log(clasificarYeison(85));

// TIP: Usa rangos con operadores lógicos para clasificar valores dentro de categorías específicas.