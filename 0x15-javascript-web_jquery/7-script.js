$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, status) {
    if (status === 'success') {
      $('#character').text(data.name);
    } else {
      $('#character').text('Failed to load character data');
    }
  });
});
