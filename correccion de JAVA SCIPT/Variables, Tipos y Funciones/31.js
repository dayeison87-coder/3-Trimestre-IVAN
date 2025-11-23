import fs from 'fs';

const davidLinea = "--- Nueva entrada: Verificación OK\n";

fs.appendFile('log.txt', davidLinea, (YeisonErr) => {
if (YeisonErr) {
console.error("Error:", YeisonErr);
return;
}
console.log("Dato agregado (APPEND)");
});

// TIP: appendFile agrega contenido al final del archivo sin borrar lo anterior.