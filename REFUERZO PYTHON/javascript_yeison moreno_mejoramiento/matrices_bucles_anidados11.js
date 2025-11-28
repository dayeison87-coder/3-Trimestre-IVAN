let yeison_moreno2 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

function imprimirLarrota(cuervo) {
  for (let yeison_moreno2 = 0; yeison_moreno2 < cuervo.length; yeison_moreno2++) {
    for (let cuervoIndex = 0; cuervoIndex < cuervo[yeison_moreno2].length; cuervoIndex++) {
      console.log(`[${yeison_moreno2}][${cuervoIndex}] = ${cuervo[yeison_moreno2][cuervoIndex]}`);
    }
  }
}

imprimirLarrota(yeison_moreno2);