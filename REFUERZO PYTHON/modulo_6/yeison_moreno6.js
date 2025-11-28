class moreno {
  constructor(nombre) {
    this.nombre = nombre;
  }

  saludar() {
    console.log("Hola " + this.nombre);
  }
}

let persona = new yeison("moreno");
persona.saludar();
