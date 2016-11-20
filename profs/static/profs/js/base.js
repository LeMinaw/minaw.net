$(document).ready(function() {
    $.taconite.debug = false;

    $("select").material_select();
    $(".button-collapse").sideNav();

    $("select").on("change", function() {
        $.post("", $("#form").serialize()); // Sending form thru AJAX
    });
});
