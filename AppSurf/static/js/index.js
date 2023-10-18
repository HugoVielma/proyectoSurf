document.addEventListener("DOMContentLoaded", function () {
  const enlaces = document.querySelectorAll("a");

  enlaces.forEach(function (enlace) {
    enlace.addEventListener("click", function (event) {
      event.preventDefault();
      const destino = enlace.getAttribute("href");

      window.location.href = destino;
    });
  });
});
