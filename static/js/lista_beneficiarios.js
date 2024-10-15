const filtrosBusquedaAvanzada = document.getElementById("filtrosBusquedaAvanzada");
  const buttonBusquedaAvanzada = document.getElementById("consultaavan");

  function ocultarMostrarBusqueda() {
    console.log("CLICK BOTON OCULTAR MOSTRAR")
      if (filtrosBusquedaAvanzada.style.display === 'none' || filtrosBusquedaAvanzada.style.display === '') {
          filtrosBusquedaAvanzada.style.display = 'block'; // Muestra el elemento
      } else {
          filtrosBusquedaAvanzada.style.display = 'none'; // Oculta el elemento
      }
  }

  // Asocia la función al evento click del botón
  buttonBusquedaAvanzada.onclick = ocultarMostrarBusqueda; 