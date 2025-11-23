import fs from 'fs';

const archivoYeison = "temporal.txt";

if (fs.existsSync(archivoYeison)) {
try {
fs.unlinkSync(archivoYeison);
console.log(`Archivo '${archivoYeison}' eliminado exitosamente`);
} catch (davidErr) {
console.error("Error al eliminar:", davidErr);
}
} else {
console.log(`El archivo '${archivoYeison}' no existe`);
}

// TIP: unlinkSync elimina archivos de forma síncrona; útil para limpieza rápida si el archivo existe.