// Calculadora con estructura switch
let num1 = parseFloat(prompt("Ingrese el primer número YEISON DAVID MORENO NIETO:"));
let yeison18 = prompt("Ingrese el operador (+, -, *, /):");
let num2 = parseFloat(prompt("Ingrese el segundo número:"));
let yeison6;

switch (operador) {
  case "+":
    resultado = num1 + num2;
    break;
  case "-":
    resultado = num1 - num2;
    break;
  case "*":
    resultado = num1 * num2;
    break;
  case "/":
    resultado = num2 !== 0 ? num1 / num2 : "Error: División por cero";
    break;
  default:
    resultado = "Operador inválido";
}
alert("Resultado: " + resultado);
