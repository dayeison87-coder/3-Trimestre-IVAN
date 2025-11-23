let YeisonDavid = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
];

function imprimirYeison(arrDavid) {
for (let Yeison = 0; Yeison < arrDavid.length; Yeison++) {
for (let david = 0; david < arrDavid[Yeison].length; david++) {
console.log(`[${Yeison}][${david}] = ${arrDavid[Yeison][david]}`);
}
}
}

imprimirYeison(YeisonDavid);