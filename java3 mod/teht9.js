'use strict';
const input = document.getElementById('calculation');
const button = document.getElementById('start');
const resultElement = document.getElementById('result');

// Tapahtumankuuntelija napille
button.addEventListener('click', () => {
  const calculation = input.value.trim();

  let result;

  try {
    if (calculation.includes('+')) {
      const [num1, num2] = calculation.split('+').map(Number);
      if (isNaN(num1) || isNaN(num2)) throw new Error('Virheellinen syöte');
      result = num1 + num2;
    } else if (calculation.includes('-')) {
      const [num1, num2] = calculation.split('-').map(Number);
      if (isNaN(num1) || isNaN(num2)) throw new Error('Virheellinen syöte');
      result = num1 - num2;
    } else if (calculation.includes('*')) {
      const [num1, num2] = calculation.split('*').map(Number);
      if (isNaN(num1) || isNaN(num2)) throw new Error('Virheellinen syöte');
      result = num1 * num2;
    } else if (calculation.includes('/')) {
      const [num1, num2] = calculation.split('/').map(Number);
      if (isNaN(num1) || isNaN(num2) || num2 === 0) throw new Error('Virheellinen syöte');
      result = Math.floor(num1 / num2);
    } else {
      throw new Error('Virheellinen operaattori');
    }

    resultElement.textContent = `Tulos: ${result}`;
  } catch (error) {
    resultElement.textContent = `Virhe: ${error.message}`;
  }
});
