let tareasYeison = [
"Hacer cama",
"Comprar pan",
"Estudiar JS",
"Lavar platos"
];

console.log("Inicial:", tareasYeison);

tareasYeison.splice(1, 1, "Pasear al perro");

console.log("Final:", tareasYeison);

// TIP: splice() modifica el array original y retorna un array con los elementos eliminados.