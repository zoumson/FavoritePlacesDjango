$(document).ready(() => {
  //alert($(location).attr('pathname'));

  // Weather data
  $('#submit-weather').click(function () {
    fetch(
      'https://api.openweathermap.org/data/2.5/weather?q=' +
        $('#enter-city').val() +
        '&units=metric' +
        '&appid=bc6c6338b16561ff04f1d3629252b86e'
    )
      .then((response) => response.json())
      .then((data) => {
        console.log('Success:', data);
        var tempValue = data['main']['temp'];
        var nameValue = data['name'];
        var descValue = data['weather'][0]['description'];
        $('#city-name').html(nameValue);
        $('#city-desc').html('Desc - ' + descValue);
        $('#city-temp').html('Temp - ' + tempValue);
        $('#enter-city').val('Enter City');
      })
      .catch((error) => {
        console.error('Error:', error);
      }); // end of fetch
  });

  // end of weather data

  // Quote of the day
  fetch('https://quotes.rest/qod?language=en')
    .then((response) => response.json())
    .then((data) => {
      var quoteValue = data['contents']['quotes'][0]['quote'];
      var authorValue = data['contents']['quotes'][0]['author'];
      $('#quote-text').html(quoteValue);
      $('#quote-author').html(authorValue);
    })
    .catch((error) => {
      console.error('Error:', error);
    }); // end of fetch

  // End of the quote of the day

  /* Make current nav bar active */
  $.each($('#ul-navbar a'), (index, value) => {
    if ($(location).attr('pathname') === $(value).attr('href')) {
      if (!$(value).hasClass('active')) {
        $(value).addClass('active');
        $('title').html($(value).html());
      }
    } else if ($(value).hasClass('active')) $(value).removeClass('active');
  });
  /* End of Make current nav bar active */
  /* Start of hide or show title of about description */
  $.each($('.data-title'), (index, value) => {
    $(value).click(() => {
      $(value).next().toggle('slow');
    });
  });

  if ($(location).attr('pathname') === '/messageSubmission') {
    if (!$('#contact').hasClass('active')) {
      $('#contact').addClass('active');
      $('title').html($('#contact').html());
    }
  }
  if ($(location).attr('pathname') === '/addPlaceSubmission') {
    if (!$('#home').hasClass('active')) {
      $('#home').addClass('active');
      $('title').html($('#home').html());
    }
  }
});
