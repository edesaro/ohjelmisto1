function kysyNumerotJaTulosta() {
    const numerot = [];

    for (let i = 0; i < 5; i++) {
        const syöte = prompt(`Anna numero ${i + 1}:`);
        const numero = Number(syöte);
        if (!isNaN(numero)) {
            numerot.push(numero);
        } else {
            alert("Syötä vain numeroita!");
            i--;
        }
    }

    console.log("Numerot käänteisessä järjestyksessä:");
    for (let i = numerot.length - 1; i >= 0; i--) {
        console.log(numerot[i]);
    }
}


document.getElementById("aloita").addEventListener("click", kysyNumerotJaTulosta);
