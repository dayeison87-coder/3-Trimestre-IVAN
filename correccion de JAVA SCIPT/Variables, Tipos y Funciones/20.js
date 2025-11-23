class AutoYeison {
constructor(davidMarca, davidModelo) {
this.davidMarca = davidMarca;
this.davidModelo = davidModelo;
}

obtenerDescripcionYeison() {
return `Marca: ${this.davidMarca}, Modelo: ${this.davidModelo}`;
}
}

const miYeisonAuto = new AutoYeison("Toyota", "Corolla");
console.log(miYeisonAuto.obtenerDescripcionYeison());

export default AutoYeison;

// TIP: Las clases permiten encapsular propiedades y métodos para representar objetos con comportamiento.