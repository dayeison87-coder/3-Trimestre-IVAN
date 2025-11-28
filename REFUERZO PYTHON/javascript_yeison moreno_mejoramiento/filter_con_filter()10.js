
let yeison_moreno1 = [15, 22, 33, 45, 68, 82, 91];
let yeison_moreno2 = yeison_moreno1.filter(temp => temp > 50);
console.log("Originales:", yeison_moreno1);
console.log("Mayores a 50:", yeison_moreno2);


//TIP: filter() es perfecto para buscar elementos que cumplan ciertos criterios sin modificar el array original.
//Úsalo cuando necesites extraer subconjuntos de datos basados en condiciones.