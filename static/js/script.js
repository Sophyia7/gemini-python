$(document).ready(function () {
  $('#chatform').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
      type: 'POST',
      url: '/chat',
      data: {
        message: $('#message').val(),
      },
      success: function (response) {
        $('#chatbox').append(
          '<p class="user-message" style="margin: 0 0 10px; text-align: center;">You: ' +
            $('#message').val() +
            '</p>'
        );
        $('#chatbox').append(
          '<p class="gemini-message" style="margin: 0 0 10px; text-align: center;">Gemini: ' +
            response.message +
            '</p>'
        );
        $('#message').val('');
      },
    });
  });
});