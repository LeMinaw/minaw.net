$(document).ready(function() { // Waiting for dynamic page generation
    var clickedwords = [];
    $('.result').on('click', function() { // Triggers on all results
        if (clickedwords.indexOf(this) == -1) {
            $.ajax({
                context: this, // We use 'this' keyword in sucess ajax event below...
                url: 'l/',
                method: 'POST',
                data: {
                    resultclicked: $(this).attr('id'), // Sends the ID of the clicked word result
                    clicked: true // Some security
                },
                success: function() {
                    clickedwords.push(this);
                    $(this).css('color', '#e04070');
                    $('#' + $(this).attr('id') + ' > .like').css('color',      '#e04070');
                    $('#' + $(this).attr('id') + ' > .like').css('visibility', 'visible');
                }
            });
        }
    });
});

// All code below used to CSRF token extraction from cookies, header setting, etc.

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
