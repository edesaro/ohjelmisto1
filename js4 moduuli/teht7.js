let map;

document.getElementById('addressForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const address = document.getElementById('address').value;
    getCoordinates(address);
});

function getCoordinates(address) {
    fetch(`https://nominatim.openstreetmap.org/search?format=json&q=${address}`)
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                const userCoords = [data[0].lat, data[0].lon];
                const schoolCoords = [60.2206, 24.8055];
                showRoute(userCoords, schoolCoords);
            } else {
                alert('Osoitetta ei löytynyt.');
            }
        });
}

function showRoute(userCoords, schoolCoords) {
    if (map) {
        map.remove();
    }
    map = L.map('map').setView(userCoords, 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    const userMarker = L.marker(userCoords).addTo(map).bindPopup('Lähtöpaikka').openPopup();
    const schoolMarker = L.marker(schoolCoords).addTo(map).bindPopup('Karaportti 2').openPopup();

    const route = L.polyline([userCoords, schoolCoords], { color: 'blue' }).addTo(map);


    const startTime = new Date();
    const endTime = new Date(startTime.getTime() + 30 * 60000);
    document.getElementById('times').innerText = `Lähtöaika: ${startTime.toLocaleTimeString()} - Saapumisaika: ${endTime.toLocaleTimeString()}`;
}