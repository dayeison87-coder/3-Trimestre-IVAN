import fs from 'fs';

fs.readFile('log.txt', 'utf8', (YeisonErr, davidData) => {
if (YeisonErr) {
console.error("Error al leer:", YeisonErr);
return;
}

console.log("=== Contenido de log.txt ===");
console.log(davidData);
console.log("============================");
});

// TIP: readFile permite leer archivos de forma asíncrona, útil para mostrar contenido sin bloquear el flujo.