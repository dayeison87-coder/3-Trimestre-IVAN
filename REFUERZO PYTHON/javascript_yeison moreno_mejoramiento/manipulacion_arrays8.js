// ejercicio08.js
let yeison_moreno1 = ["El Quijote", "100 Años de Soledad", "Fahrenheit 451"];
console.log("Libros iniciales:", yeison_moreno1.length); // 3
// Agregar al final
yeison_moreno1.push("Moby Dick");
console.log("Después de push:", yeison_moreno1.length); // 4
console.log("Libros:", yeison_moreno1);
// Remover del final
let yeison_moreno2 = yeison_moreno1.pop();
console.log("Libro removido:", yeison_moreno2); // "Moby Dick"
console.log("Libros finales:", yeison_moreno1.length); // 3