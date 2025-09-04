console.log("hola");

document.addEventListener("DOMContentLoaded", function () {
  const assistantButton = document.getElementById("assistantButton");
  const assistantChat = document.getElementById("assistantChat");
  const closeChatButton = document.getElementById("closeChat");
  const virtualAssistantContainer = document.getElementById(
    "virtualAssistantContainer"
  );

  // Función para mostrar el chat
  assistantButton.addEventListener("click", function () {
    // Ocultar el botón con animación
    assistantButton.classList.add("slide-leave-to");
    assistantButton.classList.remove("slide-enter-from");

    // Termina la animación de salida para ocultar el botón y mostrar el chat
    setTimeout(() => {
      assistantButton.classList.add("hidden");
      assistantButton.classList.remove("slide-leave-to"); // Limpiar la clase de salida

      // Mostrar el chat con animación de entrada
      assistantChat.classList.remove("hidden");
      assistantChat.classList.add("slide-enter-from");
      // Forzar reflow para que la transición se aplique desde el estado inicial
      void assistantChat.offsetWidth;
      assistantChat.classList.remove("slide-enter-from"); // Activar la transición
    }, 500); // Duración de la animación en CSS
  });

  // Función para ocultar el chat
  closeChatButton.addEventListener("click", function () {
    // Ocultar el chat con animación
    assistantChat.classList.add("slide-leave-to");
    assistantChat.classList.remove("slide-enter-from");

    setTimeout(() => {
      assistantChat.classList.add("hidden");
      assistantChat.classList.remove("slide-leave-to");

      // Mostrar el botón con animación de entrada
      assistantButton.classList.remove("hidden");
      assistantButton.classList.add("slide-enter-from");
      // Forzar reflow
      void assistantButton.offsetWidth;
      assistantButton.classList.remove("slide-enter-from"); // Activar la transición
    }, 500); // Duración de la animación en CSS
  });
});
