let david9 = parseFloat(prompt("Monto de la cuenta YEISON DAVID MORENO NIETO:"));
let yeison10 = parseInt(prompt("Porcentaje de propina (10, 15 o 20):"));
let total = cuenta + (cuenta * propina / 100);
alert(`Total con propina: $${total.toFixed(2)}`);
