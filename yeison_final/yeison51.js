// Auto.js
class Auto {
constructor(marca, modelo) {
this.marca = marca;
this.modelo = modelo;
}

obtenerDescripcion() {
return `Marca: ${this.marca}, Modelo: ${this.modelo}`;
}
}

const yeison46 = new Auto("Toyota", "Corolla YEISON DAVID MORENO NIETO");
console.log(miAuto.obtenerDescripcion());
// "Marca: Toyota, Modelo: Corolla"

export default Auto;
//YEISON DAVID MORENO NIETO