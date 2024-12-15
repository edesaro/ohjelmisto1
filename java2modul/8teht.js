document.getElementById("aloita").addEventListener("click", () => {
    const ehdokkaidenMäärä = Number(prompt("Kuinka monta ehdokasta?"));
    if (isNaN(ehdokkaidenMäärä) || ehdokkaidenMäärä <= 0) {
        alert("Anna kelvollinen määrä ehdokkaita!");
        return;
    }

    const ehdokkaat = [];
    for (let i = 0; i < ehdokkaidenMäärä; i++) {
        const nimi = prompt(`Anna nimi ehdokkaalle ${i + 1}:`);
        if (nimi.trim() !== "") {
            ehdokkaat.push({ name: nimi.trim(), votes: 0 });
        } else {
            alert("Nimi ei voi olla tyhjä!");
            i--;
        }
    }

    const äänestäjienMäärä = Number(prompt("Kuinka monta äänestäjää?"));
    if (isNaN(äänestäjienMäärä) || äänestäjienMäärä <= 0) {
        alert("Anna kelvollinen määrä äänestäjiä!");
        return;
    }


    for (let i = 0; i < äänestäjienMäärä; i++) {
        const ääni = prompt(`Äänestäjä ${i + 1}, ketä äänestät? (Anna ehdokkaan nimi tai jätä tyhjäksi tyhjälle äänelle)`);
        if (ääni.trim() !== "") {
            const ehdokas = ehdokkaat.find(e => e.name.toLowerCase() === ääni.trim().toLowerCase());
            if (ehdokas) {
                ehdokas.votes++;
            } else {
                alert("Ääntä ei hyväksytty, sillä nimeä ei löytynyt ehdokkaista.");
            }
        }
    }

    ehdokkaat.sort((a, b) => b.votes - a.votes);

    const voittaja = ehdokkaat[0];
    const tuloksetElementti = document.getElementById("tulokset");
    tuloksetElementti.textContent = `Voittaja on ${voittaja.name} ${voittaja.votes} äänellä.\n\nTulokset:\n`;

    ehdokkaat.forEach(e => {
        tuloksetElementti.textContent += `${e.name}: ${e.votes} ääntä\n`;
    });

    console.log(`Voittaja on ${voittaja.name} ${voittaja.votes} äänellä.`);
    console.log("Tulokset:");
    ehdokkaat.forEach(e => {
        console.log(`${e.name}: ${e.votes} ääntä`);
    });
});
