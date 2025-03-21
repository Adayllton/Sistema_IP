// Alternância de abas para as diferentes modalidades de parcelamento
function switchTab(tabId) {
  const tabs = document.querySelectorAll('.tab');
  const tabContents = document.querySelectorAll('.tab-content');
  
  tabs.forEach(tab => tab.classList.remove('active'));
  tabContents.forEach(content => content.classList.remove('active'));
  
  document.getElementById(tabId).classList.add('active');
  document.querySelector(`[onclick="switchTab('${tabId}')"]`).classList.add('active');
}

// Rolagem suave para seções (ex.: quando clicar em um item do menu)
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  if (section) {
    section.scrollIntoView({ behavior: 'smooth' });
  }
}

// Funções de cálculo de parcelas

function getRate(installments) {
  const rates = {
    1: 3.5, 2: 4.5, 3: 6.5, 4: 7, 5: 7.5, 6: 8, 7: 8.5, 8: 9.5, 9: 10.5,
    10: 11.5, 11: 13, 12: 13, 13: 14.5, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19
  };
  return rates[installments] / 100;
}

function getRatelink(installments) {
  const rates = {
    1: 7, 2: 9, 3: 10, 4: 11, 5: 12, 6: 14, 7: 15, 8: 16, 9: 17,
    10: 18, 11: 19, 12: 20
  };
  return rates[installments] / 100;
}

function getRatecredi(installments) {
  const rates = { 1: 5, 2: 8, 3: 10, 4: 14, 5: 17, 6: 20 };
  return rates[installments] / 100;
}

// Presencial
function calculateInstallmentSingle() {
  const value = parseFloat(document.getElementById('value').value);
  const down_payment = parseFloat(document.getElementById('down-payment').value);
  const installments = parseInt(document.getElementById('installments').value);
  const rate = getRate(installments);
  const modalidade = "Presencial";

  if (isNaN(value) || isNaN(installments) || installments < 1 || installments > 18) {
    document.getElementById('result-presencial').innerText = "Por favor, insira valores válidos (Presencial, até 18x)";
    return;
  }

  const totalValue = (value - down_payment) * (1 + rate);
  const installmentValue = totalValue / installments;
  const resultText = `Parcelando em ${installments}x: fica um investimento mensal de apenas ${installmentValue.toFixed(2)}$`;
  document.getElementById('result-presencial').innerHTML = resultText;
  document.getElementById('last-presencial').innerText = resultText;
  saveToHistory(value, modalidade, installments, totalValue, installmentValue, down_payment);
}

// Via Link
function calculateLinkInstallmentSingle() {
  const value = parseFloat(document.getElementById('value').value);
  const installments = parseInt(document.getElementById('installments').value);
  const down_payment = parseFloat(document.getElementById('down-payment').value);
  const rate = getRatelink(installments);
  const modalidade = "Via Link";

  if (isNaN(value) || isNaN(installments) || installments < 1 || installments > 12) {
    document.getElementById('result-link').innerText = "Por favor, insira valores válidos (Via Link, até 12x)";
    return;
  }

  const totalValue = (value - down_payment) * (1 + rate);
  const installmentValue = totalValue / installments;
  const resultText = `Parcelando em ${installments}x: fica um investimento mensal de apenas ${installmentValue.toFixed(2)}$`;
  document.getElementById('result-link').innerHTML = resultText;
  document.getElementById('last-link').innerText = resultText;
  saveToHistory(value, modalidade, installments, totalValue, installmentValue, down_payment);
}

// Credishop
function calculateInstallmentCrediSingle() {
  const value = parseFloat(document.getElementById('value').value);
  const down_payment = parseFloat(document.getElementById('down-payment').value);
  const installments = parseInt(document.getElementById('installments').value);
  const rate = getRatecredi(installments);
  const modalidade = "Credishop";

  if (isNaN(value) || isNaN(installments) || installments < 1 || installments > 6) {
    document.getElementById('result-credi').innerText = "Por favor, insira valores válidos (Credishop, até 6x)";
    return;
  }

  const totalValue = (value - down_payment) * (1 + rate);
  const installmentValue = totalValue / installments;
  const resultText = `Parcelando em ${installments}x: fica um investimento mensal de apenas ${installmentValue.toFixed(2)}$`;
  document.getElementById('result-credi').innerHTML = resultText;
  document.getElementById('last-credi').innerText = resultText;
  saveToHistory(value, modalidade, installments, totalValue, installmentValue, down_payment);
}

// Calcular Todas - Presencial
function calculateAllInstallment() {
  const value = parseFloat(document.getElementById('value').value);
  const down_payment = parseFloat(document.getElementById('down-payment').value);
  const resultElement = document.getElementById('result-presencial');

  if (isNaN(value)) {
    resultElement.innerText = "Por favor, insira valores válidos.";
    return;
  }

  let resultados = '';
  let lastCalculation = '';
  for (let parcelas = 1; parcelas <= 18; parcelas++) {
    const rate = getRate(parcelas);
    const totalValue = (value - down_payment) * (1 + rate);
    const installmentValue = totalValue / parcelas;
    lastCalculation = `Parcelando em ${parcelas}x: fica um investimento mensal de${installmentValue.toFixed(2)}$`;
    resultados += lastCalculation + "<br><br>";
  }
  resultElement.innerHTML = resultados;
  document.getElementById('last-presencial').innerText = lastCalculation;
}

// Calcular Todas - Via Link
function calculateAllLinkInstallment() {
  const value = parseFloat(document.getElementById('value').value);
  const installments = parseInt(document.getElementById('installments').value);
  const down_payment = parseFloat(document.getElementById('down-payment').value);
  const resultElement = document.getElementById('result-link');

  if (isNaN(value)) {
    resultElement.innerText = "Por favor, insira valores válidos.";
    return;
  }

  let resultados = '';
  let lastCalculation = '';
  for (let parcelas = 1; parcelas <= 12; parcelas++) {
    const rate = getRatelink(parcelas);
    const totalValue = (value - down_payment) * (1 + rate);
    const installmentValue = totalValue / parcelas;
    lastCalculation = `Parcelando em ${parcelas}x: fica um investimento mensal de${installmentValue.toFixed(2)}$`;
    resultados += lastCalculation + "<br><br>";
  }
  resultElement.innerHTML = resultados;
  document.getElementById('last-link').innerText = lastCalculation;
}

// Calcular Todas - Credishop
function calculateAllCrediInstallment() {
  const value = parseFloat(document.getElementById('value').value);
  const installments = parseInt(document.getElementById('installments').value);
  const down_payment = parseFloat(document.getElementById('down-payment').value);
  const resultElement = document.getElementById('result-credi');

  if (isNaN(value)) {
    resultElement.innerText = "Por favor, insira valores válidos.";
    return;
  }

  let resultados = '';
  let lastCalculation = '';
  for (let parcelas = 1; parcelas <= 6; parcelas++) {
    const rate = getRatecredi(parcelas);
    const totalValue = (value - down_payment) * (1 + rate);
    const installmentValue = totalValue / parcelas;
    lastCalculation = `Parcelando em ${parcelas}x: fica um investimento mensal de${installmentValue.toFixed(2)}$`;
    resultados += lastCalculation + "<br><br>";
  }
  resultElement.innerHTML = resultados;
  document.getElementById('last-credi').innerText = lastCalculation;
}

// Histórico e funções de cópia

function saveToHistory(value, modalidade, installments, totalValue, installmentValue, down_payment) {
  const history = JSON.parse(localStorage.getItem('history')) || [];
  history.unshift({
    value: value.toFixed(2),
    installments: installments,
    modalidade: modalidade,
    down_payment: down_payment,
    totalValue: totalValue.toFixed(2),
    installmentValue: installmentValue.toFixed(2)
  });
  localStorage.setItem('history', JSON.stringify(history));
  displayHistory();
}

function displayHistory() {
  const history = JSON.parse(localStorage.getItem('history')) || [];
  const historyList = document.getElementById('history-list');
  historyList.innerHTML = history.map(item => `
      <div class="parcela-calculada">
          Valor: R$ ${item.value} - Entrada: R$ ${item.down_payment} - <b>${item.modalidade}</b> em <b>${item.installments}x</b><br>
          Total: R$ ${item.totalValue} - Parcela: <b>R$ ${item.installmentValue}</b>
      </div>
  `).join('');
}

function clearHistory() {
  localStorage.removeItem('history');
  displayHistory();
}

function copyToClipboard(elementId) {
  // Obtém o texto do elemento indicado pelo ID
  const resultText = document.getElementById(elementId).innerText;
  // Cria um textarea temporário
  const tempInput = document.createElement('textarea');
  tempInput.value = resultText;
  document.body.appendChild(tempInput);
  // Seleciona o conteúdo e copia para a área de transferência
  tempInput.select();
  document.execCommand('copy');
  // Remove o elemento temporário
  document.body.removeChild(tempInput);
  alert("Resultado copiado para a área de transferência!");
}


function copyToClipboardPresencial() {
  copyToClipboard('result-presencial');
}

function copyToClipboardLink() {
  copyToClipboard('result-link');
}

function copyToClipboardCredi() {
  copyToClipboard('result-credi');
}

function copyCalcResult() {
  copyToClipboard('calc-result');
}

function calculateBasic() {
  const num1 = parseFloat(document.getElementById('calc-num1').value);
  const num2 = parseFloat(document.getElementById('calc-num2').value);
  const operator = document.getElementById('calc-operator').value;
  let result;
  if (isNaN(num1) || isNaN(num2)) {
    result = "Insira números válidos.";
  } else {
    switch (operator) {
      case '+': result = num1 + num2; break;
      case '-': result = num1 - num2; break;
      case '*': result = num1 * num2; break;
      case '/': result = num2 !== 0 ? num1 / num2 : "Divisão por zero!"; break;
      case '%': result = num2 !== 0 ? (num1 / num2) * 100 + "%" : "Divisão por zero!"; break;
      default: result = "Operador inválido.";
    }
  }
  document.getElementById('calc-result').innerText = "Resultado: " + result;
}

function calculateBasicStandalone() {
  const num1 = parseFloat(document.getElementById('calc-num1-standalone').value);
  const num2 = parseFloat(document.getElementById('calc-num2-standalone').value);
  const operator = document.getElementById('calc-operator-standalone').value;
  let result;
  if (isNaN(num1) || isNaN(num2)) {
    result = "Insira números válidos.";
  } else {
    switch (operator) {
      case '+': result = num1 + num2; break;
      case '-': result = num1 - num2; break;
      case '*': result = num1 * num2; break;
      case '/': result = num2 !== 0 ? num1 / num2 : "Divisão por zero!"; break;
      case '%': result = num2 !== 0 ? (num1 / num2) * 100 + "%" : "Divisão por zero!"; break;
      default: result = "Operador inválido.";
    }
  }
  document.getElementById('calc-result-standalone').innerText = "Resultado: " + result;
}

function copyCalcResultStandalone() {
  copyToClipboard('calc-result-standalone');
}

window.onload = displayHistory;
