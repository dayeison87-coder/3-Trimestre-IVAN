let yeison_moreno1 = ["Cliente A", "Cliente B", "Cliente C"];
console.log("Cola inicial:", yeison_moreno1);

let yeison_moreno2 = yeison_moreno1.shift();
console.log("Cliente atendido:", yeison_moreno2);
console.log("Cola después de shift:", yeison_moreno1);

yeison_moreno1.unshift("Cliente Prioritario");
console.log("Cola final:", yeison_moreno1);

//shift() - Remover del inicioElimina y retorna el primer elemento. Todos losdemás elementos se desplazan una posición haciaadelante.
//unshift() - Agregar al inicioAñade elementos al inicio. Todos los elementos existentes se desplazan una posición hacia atrás.