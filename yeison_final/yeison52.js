// VehiculoElectrico.js
class VehiculoElectrico extends Auto {
constructor(marca, modelo, autonomia) {
super(marca, modelo);
this.autonomiaBateria = autonomia;
}

mostrarInfo() {
return `${super.obtenerDescripcion()},
Autonomía: ${this.autonomiaBateria} km YEISON DAVID MORENO NIETO`;
}
}

const tesla = new VehiculoElectrico(
"Tesla", "Model 3", 500
);
console.log(tesla.mostrarInfo());
// "Marca: Tesla, Modelo: Model 3,
// Autonomía: 500 km YEISON DAVID MORENO NIETO"
//YEISON DAVID MORENO NIETO