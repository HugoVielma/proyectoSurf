document.addEventListener("DOMContentLoaded", function () {
  const enlaces = document.querySelectorAll("a");

  enlaces.forEach(function (enlace) {
    enlace.addEventListener("click", function (event) {
      event.preventDefault(); // Esto evita el comportamiento de salto
      const destino = enlace.getAttribute("href");

      // Luego puedes redirigir a la URL de destino utilizando JavaScript
      window.location.href = destino;
    });
  });
});
