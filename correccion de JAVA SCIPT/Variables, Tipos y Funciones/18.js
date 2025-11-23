const verificarYeison = (davidEdad) =>
davidEdad >= 18 ? "Permitido" :
"Denegado";

console.log("17 años:",
verificarYeison(17));

console.log("35 años:",
verificarYeison(35));

// TIP: El operador ternario permite evaluar condiciones de forma compacta y legible.