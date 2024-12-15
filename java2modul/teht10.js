let candidates = [];

document.getElementById('candidateForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const numCandidates = parseInt(document.getElementById('numCandidates').value);
    const candidateInputsDiv = document.getElementById('candidateInputs');
    candidateInputsDiv.innerHTML = ''; // Tyhjennetään vanhat syötteet

    for (let i = 0; i < numCandidates; i++) {
        const input = document.createElement('input');
        input.type = 'text';
        input.placeholder = `Ehdokkaan ${i + 1} nimi`;
        input.required = true;
        candidateInputsDiv.appendChild(input);
    }

    const submitButton = document.createElement('button');
    submitButton.textContent = 'Tallenna ehdokkaat';
    submitButton.addEventListener('click', function() {
        candidates = [];
        const inputs = candidateInputsDiv.querySelectorAll('input');
        inputs.forEach(input => {
            candidates.push({ name: input.value, votes: 0 });
        });
        document.getElementById('voterForm').style.display = 'block';
    });
    candidateInputsDiv.appendChild(submitButton);
});

document.getElementById('voterForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const numVoters = parseInt(document.getElementById('numVoters').value);
    const voterInputsDiv = document.getElementById('voterInputs');
    voterInputsDiv.innerHTML = ''; // Tyhjennetään vanhat syötteet

    for (let i = 0; i < numVoters; i++) {
        const input = document.createElement('input');
        input.type = 'text';
        input.placeholder = `Äänestäjä ${i + 1}`;
        voterInputsDiv.appendChild(input);
    }

    document.getElementById('votingSection').style.display = 'block';
});

document.getElementById('voteButton').addEventListener('click', function() {
    const voterInputs = document.getElementById('voterInputs').querySelectorAll('input');
    voterInputs.forEach(input => {
        const vote = input.value;
        if (vote) {
            const candidate = candidates.find(c => c.name.toLowerCase() === vote.toLowerCase());
            if (candidate) {
                candidate.votes++;
            } else {
                console.log(`Virheellinen ääni: ${vote}.`);
            }
        } else {
            console.log("Tyhjä ääni.");
        }
    });

    announceResults(candidates);
});

function announceResults(candidates) {
    candidates.sort((a, b) => b.votes - a.votes);
    const winner = candidates[0];
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `Voittaja on ${winner.name} ${winner.votes} äänellä.<br>Tulokset:<br>`;
    candidates.forEach(candidate => {
        resultsDiv.innerHTML += `${candidate.name}: ${candidate.votes} ääntä<br>`;
    });
}