$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
    if (status === 'success') {
      const films = data.results;
      $.each(films, function (index, film) {
        $('#list_movies').append('<li>' + film.title + '</li>');
      });
    } else {
      $('#list_movies').text('Failed to load data');
    }
  });
});
