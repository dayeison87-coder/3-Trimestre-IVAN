const yeison_moreno1 = (cuervoBase, cuervoAltura) => {
  return (cuervoBase * cuervoAltura) / 2;
};

const yeison_moreno2 = (cuervoBase, cuervoAltura) =>
  (cuervoBase * cuervoAltura) / 2;

console.log("Área:", yeison_moreno1(8, 5));

// TIP: Puedes usar funciones flecha con return implícito para simplificar cálculos como este.