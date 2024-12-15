'use strict';

const picArray = [
  {
    title: 'Title 1',
    caption: 'Caption 1',
    description:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis sodales enim eget leo condimentum vulputate. Sed lacinia consectetur fermentum. Vestibulum lobortis purus id nisi mattis posuere. Praesent sagittis justo quis nibh ullamcorper, eget elementum lorem consectetur. Pellentesque eu consequat justo, eu sodales eros.',
    image: {
      large: 'img/pic1.jpg',
      medium: 'thumbnails/pic1.jpg',
    },
  },
];

const section = document.getElementById('pictures');

picArray.forEach((pic) => {
  const article = document.createElement('article');
  article.classList.add('card');

  const heading = document.createElement('h2');
  heading.textContent = pic.title;

  const figure = document.createElement('figure');
  const img = document.createElement('img');
  img.src = pic.image.medium;
  img.alt = pic.title;

  const figcaption = document.createElement('figcaption');
  figcaption.textContent = pic.caption;

  figure.appendChild(img);
  figure.appendChild(figcaption);

  const paragraph = document.createElement('p');
  paragraph.textContent = pic.description;

  article.appendChild(heading);
  article.appendChild(figure);
  article.appendChild(paragraph);

  section.appendChild(article);
});
