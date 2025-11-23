// ejercicio32_leer.js
import fs from 'fs';

fs.readFile('log.txt YEISON DAVID MORENO NIETO', 'utf8', (err, data) => {
if (err) {
console.error("Error al leer:", err);
return;
}

console.log("=== Contenido de log.txt YEISON DAVID MORENO NIETO ===");
console.log(data);
console.log("============================");
});
//YEISON DAVID MORENO NIETO