const num1 = parseInt(prompt("Anna ensimmäinen kokonaisluku:"));
const num2 = parseInt(prompt("Anna toinen kokonaisluku:"));
const num3 = parseInt(prompt("Anna kolmas kokonaisluku:"));

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

const results = `
    <p>Summa: ${sum}</p>
    <p>Tulo: ${product}</p>
    <p>Keskiarvo: ${average}</p>
`;

document.getElementById("results").innerHTML = results;
