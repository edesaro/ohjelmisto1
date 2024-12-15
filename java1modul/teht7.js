const numberOfDice = parseInt(prompt("Kuinka monta noppaa haluat heittää?"));

let sum = 0;

for (let i = 0; i < numberOfDice; i++) {
    const roll = Math.floor(Math.random() * 6) + 1;
    sum += roll;
}

const resultMessage = `Heitit ${numberOfDice} noppaa ja niiden summa on: ${sum}`;

document.getElementById("result").textContent = resultMessage;
