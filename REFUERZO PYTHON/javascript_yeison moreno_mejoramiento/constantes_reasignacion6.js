const yeison_moreno1 = 3.14159;
// yeison_moreno1 = 3.14; // ERROR!
console.log(yeison_moreno1); // 3.14159
//Las constantes NO pueden
//reasignarse después de
//declararse


let yeison_moreno2 = 10;

yeison_moreno2 = 20; // Válido
console.log(yeison_moreno2); // 20
//Las variables con let pueden
//cambiar de valor libremente

{
let temporal = 5;
const fija = 10;
console.log(temporal)
console.log(fija)
}
//Tanto let como const tienen ámbito
//de bloque (dentro de {})