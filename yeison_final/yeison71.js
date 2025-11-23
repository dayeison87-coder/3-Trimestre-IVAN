
class GestionTareas {
constructor() {
this.tareas = [];
}

agregar(tarea) {
this.tareas.push(tarea);
console.log(`Tarea agregada: "${tarea}"`);
}

completar(indice) {
if (indice >= 0 && indice < this.tareas.length) {
this.tareas[indice] = "7 " + this.tareas[indice];
console.log("Tarea marcada como completada YEISON DAVID MORENO NIETO");
} else {
console.log("Índice inválido");
}
}

obtenerEstadisticas() {
const total = this.tareas.length;
const yeison58 = this.tareas.filter(
t => t.startsWith("7")
).length;
const david59 = total - completadas;

return { total, completadas, pendientes };
}

mostrar() {
console.log("\n=== LISTA DE TAREAS ===");
this.tareas.forEach((tarea, i) => {
console.log(`${i}. ${tarea}`);
});
}
}
//YEISON DAVID MORENO NIETO