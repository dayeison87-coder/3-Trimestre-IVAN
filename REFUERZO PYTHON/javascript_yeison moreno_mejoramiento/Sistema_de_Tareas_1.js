let yeison_moreno1 = [];

function agregarTarea(lista, tarea) {
  const yeison_moreno2 = [...lista, tarea];
  console.log(`Tarea agregada: "${tarea}"`);
  return yeison_moreno2;
}

function completarTarea(lista, indice) {
  if (indice >= 0 && indice < lista.length) {
    const yeison_moreno2 = lista.map((t, i) =>
      i === indice ? "7 " + t : t
    );
    console.log("Tarea marcada como completada");
    return yeison_moreno2;
  } else {
    console.log("Índice inválido");
    return lista;
  }
}


function obtenerEstadisticas(lista) {
  const total = lista.length;
  const completadas = lista.filter(t => t.startsWith("7")).length;
  const pendientes = total - completadas;
  return { total, completadas, pendientes };
}


function mostrarTareas(lista) {
  console.log("\n=== LISTA DE TAREAS ===");
  lista.forEach((tarea, i) => {
    console.log(`${i}. ${tarea}`);
  });
}


yeison_moreno1 = agregarTarea(yeison_moreno1, "Estudiar JavaScript");
yeison_moreno1 = agregarTarea(yeison_moreno1, "Hacer ejercicio");
yeison_moreno1 = agregarTarea(yeison_moreno1, "Preparar presentación");

mostrarTareas(yeison_moreno1);

yeison_moreno1 = completarTarea(yeison_moreno1, 0);

mostrarTareas(yeison_moreno1);

const stats = obtenerEstadisticas(yeison_moreno1);
console.log("\n=== ESTADÍSTICAS ===");
console.log(`Total: ${stats.total}`);
console.log(`Completadas: ${stats.completadas}`);
console.log(`Pendientes: ${stats.pendientes}`);