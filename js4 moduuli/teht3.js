document.getElementById('searchForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const query = document.getElementById('query').value;
    fetchTVShows(query);
});

function fetchTVShows(query) {
    fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = ''; // Tyhjennetään vanhat tulokset

            data.forEach(tvShow => {
                const article = document.createElement('article');

                const h2 = document.createElement('h2');
                h2.textContent = tvShow.show.name;
                article.appendChild(h2);

                const a = document.createElement('a');
                a.href = tvShow.show.url;
                a.target = '_blank';
                a.textContent = 'Lisätiedot';
                article.appendChild(a);

                if (tvShow.show.image?.medium) {
                    const img = document.createElement('img');
                    img.src = tvShow.show.image.medium;
                    img.alt = tvShow.show.name;
                    article.appendChild(img);
                }

                const div = document.createElement('div');
                div.innerHTML = tvShow.show.summary;
                article.appendChild(div);

                resultsDiv.appendChild(article);
            });
        });
}