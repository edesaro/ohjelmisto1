
const year = parseInt(prompt("Anna vuosi, jonka haluat tarkistaa:"));

let message;
if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
    message = `${year} on karkausvuosi.`;
} else {
    message = `${year} ei ole karkausvuosi.`;
}

document.getElementById("result").textContent = message;
