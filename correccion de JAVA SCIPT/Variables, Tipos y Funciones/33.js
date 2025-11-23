import fs from 'fs';

function actualizarYeison(davidContenido) {
fs.writeFile('log.txt', davidContenido, (YeisonErr) => {
if (YeisonErr) {
console.error("Error:", YeisonErr);
return;
}
console.log("Archivo actualizado (UPDATE)");
});
}

const davidActualizado =
"Registro actualizado: " +
new Date().toLocaleString() + "\n";

actualizarYeison(davidActualizado);

// TIP: writeFile sobrescribe el contenido del archivo, útil para actualizaciones completas.