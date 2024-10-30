document.addEventListener("DOMContentLoaded", function() {
    const filtrosBusquedaAvanzada = document.getElementById("filtrosBusquedaAvanzada");
    const btnMostrarFiltros = document.getElementById("consultaavan");

    function ocultarMostrarBusqueda() {
        if (filtrosBusquedaAvanzada.style.display === 'none' || filtrosBusquedaAvanzada.style.display === '') {
            filtrosBusquedaAvanzada.style.display = 'block';
        } else {
            filtrosBusquedaAvanzada.style.display = 'none';
        }
    }

    btnMostrarFiltros.onclick = ocultarMostrarBusqueda;
    
});
