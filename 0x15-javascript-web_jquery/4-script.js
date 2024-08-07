$(document).ready(function () {
  $('#toggle_header').click(function () {
    const header = $('header');
    if (header.hasClass('green')) {
      header.removeClass('green').addClass('red');
    } else {
      header.removeClass('red').addClass('green');
    }
  });
});
