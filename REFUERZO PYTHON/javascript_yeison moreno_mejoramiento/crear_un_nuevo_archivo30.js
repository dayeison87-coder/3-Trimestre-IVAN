import fs from 'fs';

const yeison_moreno1 = new Date().toISOString();
const yeison_moreno2 = `Larrota log creado a las: ${yeison_moreno1}\n`;

fs.writeFile('larrota_log.txt', yeison_moreno2, (larrotaError) => {
  if (larrotaError) {
    console.error("Error Larrota:", larrotaError);
    return;
  }
  console.log("Archivo Larrota creado exitosamente (CREATE)");
});