// submit_preventer.js
// Esse script previne o envio duplicado de formulários
document.addEventListener('DOMContentLoaded', function() {
    // Seleciona todos os formulários da página
    const forms = document.querySelectorAll('form');
  
    // Para cada formulário, adiciona um listener no evento submit
    forms.forEach(function(form) {
      form.addEventListener('submit', function(event) {
        // Seleciona todos os botões de envio dentro do formulário
        const submitButtons = form.querySelectorAll('button[type="submit"]');
        // Desabilita cada botão para evitar múltiplos envios
        submitButtons.forEach(function(button) {
          button.disabled = true;
        });
        // Opcional: se o formulário for enviado via AJAX, você pode reabilitar o botão se ocorrer erro
        // event.preventDefault(); // Se necessário, para testes
      });
    });
  });
  