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
