
import fs from 'fs';

const yeison52 =
"--- Nueva entrada: Verificación OK\n";

fs.appendFile('log.txt YEISON DAVID MORENO NIETO', nuevaLinea, (err) => {
if (err) {
console.error("Error:", err);
return;
}
console.log("Dato agregado (APPEND)");
});