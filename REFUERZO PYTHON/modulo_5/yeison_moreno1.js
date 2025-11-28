import { Gift } from './clases.js';
import datosInit from '../Data/Data.json' assert { type: 'json' };

// usamos una copia mutable en memoria
let yeison_moreno1 = Array.isArray(datosInit) ? datosInit : [];

let yeison_moreno2 = null;
const cuerpoTabla = document.querySelector('#cuerpo-tabla');
const myModal = new bootstrap.Modal(document.getElementById('modal-gift'));

// Chart.js instance placeholder
let chartTipos = null;

const calcularEstadisticas = () => {
  const estadisticas = yeison_moreno1.reduce((acc, item) => {
    acc[item.tipo] = (acc[item.tipo] || 0) + 1;
    return acc;
  }, {});
  return estadisticas;
};

const actualizarChart = () => {
  const ctx = document.getElementById('chartTipos').getContext('2d');
  const estad = calcularEstadisticas();
  const labels = Object.keys(estad);
  const values = labels.map(l => estad[l]);
  if (chartTipos) { chartTipos.destroy(); chartTipos = null; }
  chartTipos = new Chart(ctx, {
    type: 'pie',
    data: { labels, datasets: [{ data: values }] },
    options: { responsive: true }
  });
};

const cargarTabla = () => {
  cuerpoTabla.innerHTML = '';
  yeison_moreno1.map((item) => {
    const fila = document.createElement('tr');
    const celdas = `
      <td>${item.gift}</td>
      <td>${item.tipo}</td>
      <td>${item.tiempo}</td>
      <td>$${item.precio}</td>
      <td>
        <div class="d-flex gap-2">
          <button class="btn btn-outline-warning" onclick="window.MostrarModal(${item.id})">
            <i class="fas fa-pencil-alt"></i>
          </button>
          <button class="btn btn-outline-danger" onclick="window.BorrarGift(${item.id})">
            <i class="fas fa-times"></i>
          </button>
        </div>
      </td>
    `;
    fila.innerHTML = celdas;
    cuerpoTabla.appendChild(fila);
  });
  actualizarChart();
};

// DELETE
window.BorrarGift = (id) => {
  const index = yeison_moreno1.findIndex((item) => item.id === id);
  if (index === -1) return;
  const validar = confirm(`¿Está seguro que quiere eliminar la gift Card ${yeison_moreno1[index].gift}?`);
  if (validar) {
    yeison_moreno1.splice(index, 1);
    cargarTabla();
    // persistir en localStorage opcional
    localStorage.setItem('misGifts', JSON.stringify(yeison_moreno1));
  }
};

// CREATE
const formAgregar = document.querySelector('#form-gift');
formAgregar.addEventListener('submit', agregarGift);

function agregarGift(e) {
  e.preventDefault();
  const id = (yeison_moreno1.at(-1)?.id || 0) + 1;
  const gift = document.querySelector('#gift').value;
  const tipo = document.querySelector('#tipo').value;
  const tiempo = document.querySelector('#tiempo').value;
  const precio = document.querySelector('#precio').value;
  const imagen = document.querySelector('#imagen').value;
  yeison_moreno1.push(new Gift(id, gift, tipo, tiempo, precio, imagen));
  formAgregar.reset();
  cargarTabla();
  localStorage.setItem('misGifts', JSON.stringify(yeison_moreno1));
}

// UPDATE - Mostrar modal
window.MostrarModal = (id) => {
  yeison_moreno2 = id;
  const index = yeison_moreno1.findIndex((item) => item.id === id);
  if (index === -1) return;
  document.querySelector('#gift-modal').value = yeison_moreno1[index].gift;
  document.querySelector('#tipo-modal').value = yeison_moreno1[index].tipo;
  document.querySelector('#tiempo-modal').value = yeison_moreno1[index].tiempo;
  document.querySelector('#precio-modal').value = yeison_moreno1[index].precio;
  document.querySelector('#imagen-modal').value = yeison_moreno1[index].imagen;
  myModal.show();
};

// UPDATE - Guardar cambios
const formModal = document.querySelector('#form-modal');
formModal.addEventListener('submit', giftUpdate);

function giftUpdate(e) {
  e.preventDefault();
  const index = yeison_moreno1.findIndex((item) => item.id === yeison_moreno2);
  if (index === -1) return;
  yeison_moreno1[index].gift = document.querySelector('#gift-modal').value;
  yeison_moreno1[index].tipo = document.querySelector('#tipo-modal').value;
  yeison_moreno1[index].tiempo = document.querySelector('#tiempo-modal').value;
  yeison_moreno1[index].precio = document.querySelector('#precio-modal').value;
  yeison_moreno1[index].imagen = document.querySelector('#imagen-modal').value;
  cargarTabla();
  myModal.hide();
  localStorage.setItem('misGifts', JSON.stringify(yeison_moreno1));
}

// Inicializar yeison_moreno1 desde localStorage si existe
const datosGuardados = localStorage.getItem('misGifts');
if (datosGuardados) {
  try { yeison_moreno1 = JSON.parse(datosGuardados); } catch (e) { yeison_moreno1 = yeison_moreno1; }
}

// Ejecutar carga inicial
cargarTabla();
