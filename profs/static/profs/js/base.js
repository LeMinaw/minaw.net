$(document).ready(function() {
    $.taconite.debug = false;

    $("select").material_select();
    $(".button-collapse").sideNav();
    $('.modal').modal();

    $("select").on("change", function() {
        $.post("", $("#form").serialize()); // Sending form thru AJAX
    });

    if ($("#thanks")) {
        $("#thanks").modal('open');
    }

});
