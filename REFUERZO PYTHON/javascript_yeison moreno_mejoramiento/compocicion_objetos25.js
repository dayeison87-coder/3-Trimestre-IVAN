class LarrotaDireccion {
  constructor(larrotaCalle, larrotaCodigoPostal) {
    this.larrotaCalle = larrotaCalle;
    this.larrotaCodigoPostal = larrotaCodigoPostal;
  }
}

class LarrotaCliente {
  constructor(larrotaNombre, larrotaDireccion) {
    this.larrotaNombre = larrotaNombre;
    this.larrotaDireccion = larrotaDireccion;
  }

  mostrarLarrotaUbicacion() {
    console.log(`${this.larrotaNombre} vive en:
${this.larrotaDireccion.larrotaCalle},
CP ${this.larrotaDireccion.larrotaCodigoPostal}`);
  }
}

const yeison_moreno1 = new LarrotaDireccion(
  "Calle de la Victoria 789", "11011"
);
const yeison_moreno2 = new LarrotaCliente("Larrota Gómez", yeison_moreno1);
yeison_moreno2.mostrarLarrotaUbicacion();