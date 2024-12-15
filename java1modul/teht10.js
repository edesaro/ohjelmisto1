document.getElementById('diceForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const dice = parseInt(document.getElementById('dice').value);
    const sum = parseInt(document.getElementById('sum').value);
    const simulations = 10000;
    let successCount = 0;

    for (let i = 0; i < simulations; i++) {
        let total = 0;
        for (let j = 0; j < dice; j++) {
            total += Math.floor(Math.random() * 6) + 1;
        }
        if (total === sum) {
            successCount++;
        }
    }

    const probability = (successCount / simulations * 100).toFixed(2);
    document.getElementById('result').innerText = `Todennäköisyys saada summa ${sum} ${dice} nopalla on ${probability}%`;
});