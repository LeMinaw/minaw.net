$(document).ready(function() {
    $('#id_name').keyup(function() {
        var short = $('#id_short'),
            slug =  $('#id_slug');
        let shortReg = /^([A-Z]{1})\S* (.*)+$/g,
            slugReg  = /^\S* (.*)+$/g;

        var shortOut = shortReg.exec($('#id_name').val()),
            slugOut  = slugReg.exec($('#id_name').val());

        short.val(shortOut[1].toUpperCase() + '. ' + shortOut[2]);
        slug.val(slugOut[1].toLowerCase().replace(' ', '-'));
    });
});
