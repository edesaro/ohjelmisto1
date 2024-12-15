'use strict';

const randomNumber = Math.random()
// else-haaran testamista varten kovakoodattu arvo
console.log('Arvottu numero', randomNumber)
//ehtolause, ehdon täytyy olla aina true/false
// 50% todennäköisyys
    if (randomNumber< 0.495) {
        console.log("Kruuna")
    } else if (randomNumber > 0.505) {
        console.log('Klaava')
    } else {
        console.log('Kolikko jää kantilleen')
    }

    console.log('Suoritus jatkuu ehtolauseen jälkeen')



// Toistorakenteet eli silmukat eli loopit
// kuinka monta heittoa menee, että jää kyljilleen?

let throwCount = 0
while (true) {
    const randomNumber = Math.random()
    throwCount++;
    if (randomNumber < 0.495) {
        console.log("Kruuna");
    } else if (randomNumber > 0.505) {
        console.log('Klaava');
    } else {
        console.log('Kolikko jää kantilleen');
        console.log('heittojen lkm', throwCount);
        break;

    }


}

