
function kysyOsallistujat() {
    const määräSyöte = prompt("Kuinka monta osallistujaa?");
    const osallistujienMäärä = Number(määräSyöte);

    if (isNaN(osallistujienMäärä) || osallistujienMäärä <= 0) {
        alert("Anna kelvollinen osallistujien määrä!");
        return;
    }

    const osallistujat = [];


    for (let i = 0; i < osallistujienMäärä; i++) {
        const nimi = prompt(`Anna osallistujan ${i + 1} nimi:`);
        if (nimi.trim() !== "") {
            osallistujat.push(nimi.trim());
        } else {
            alert("Nimi ei voi olla tyhjä!");
            i--;
        }
    }

    osallistujat.sort();

    const lista = document.getElementById("osallistujat");
    lista.innerHTML = "";
    osallistujat.forEach(nimi => {
        const listanKohde = document.createElement("li");
        listanKohde.textContent = nimi;
        lista.appendChild(listanKohde);
    });
}
document.getElementById("aloita").addEventListener("click", kysyOsallistujat);
