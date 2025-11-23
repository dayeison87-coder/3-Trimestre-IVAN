// AutoEstatico.js
class Auto {
constructor(marca, modelo) {
this.marca = marca;
this.modelo = modelo;
}

static informacionGeneral() {
return "Clase base para gestión de vehículos YEISON DAVID MORENO NIETO";
}
}

// Llamada desde la clase
console.log(Auto.informacionGeneral());

// ERROR: No funciona desde instancias
const carro = new Auto("Ford", "Focus");
// carro.informacionGeneral(); // Error
//YEISON DAVID MORENO NIETO