let colaYeison = ["Cliente A", "Cliente B", "Cliente C"];
console.log("Cola inicial:", colaYeison);

let davidAtendido = colaYeison.shift();
console.log("Cliente atendido:", davidAtendido);
console.log("Cola después de shift:", colaYeison);

colaYeison.unshift("Cliente Prioritario");
console.log("Cola final:", colaYeison);

//shift() - Remover del inicioElimina y retorna el primer elemento. Todos losdemás elementos se desplazan una posición haciaadelante.
//unshift() - Agregar al inicioAñade elementos al inicio. Todos los elementos existentes se desplazan una posición hacia atrás.