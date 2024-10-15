const filtrosBusquedaAvanzada = document.getElementById("filtrosBusquedaAvanzada");
const btnMostrarFiltros = document.getElementById("consultaavan");

function ocultarMostrarBusqueda() {
    if (filtrosBusquedaAvanzada.style.display === 'none' || filtrosBusquedaAvanzada.style.display === '') {
        filtrosBusquedaAvanzada.style.display = 'block'; // Muestra el elemento
    } else {
        filtrosBusquedaAvanzada.style.display = 'none'; // Oculta el elemento
    }
}

btnMostrarFiltros.onclick = ocultarMostrarBusqueda; 

const btnBuscar = document.getElementById("btnBuscar");
const btnBusquedaAvanzada = document.getElementById("btnBusquedaAvanzada");
const resultadosGenerales = document.getElementById("resultadosGenerales");

function ocultarMostrarResultadosGenerales() {
    if (resultadosGenerales.style.display === 'none' || resultadosGenerales.style.display === '') {
        resultadosGenerales.style.display = 'block'; // Muestra el elemento
    } else {
        resultadosGenerales.style.display = 'none'; // Oculta el elemento
    }
}