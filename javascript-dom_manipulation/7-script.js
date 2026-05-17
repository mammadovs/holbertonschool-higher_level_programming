const listMoviesElement = document.querySelector('#list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    const movies = data.results;
    movies.forEach(function (movie) {
      const newListItem = document.createElement('li');
      newListItem.textContent = movie.title;
      listMoviesElement.appendChild(newListItem);
    });
  });
