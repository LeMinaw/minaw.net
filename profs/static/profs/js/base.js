$(document).ready(function() {
    $.taconite.debug = false;

    $("select").material_select();
    $(".button-collapse").sideNav();
    $('.modal').modal();

    $("select").on("change", function() {
        $.post("", $("#form").serialize()); // Sending form thru AJAX
    });

    if ($("#thanks").length) {
        $("#thanks").modal('open');
    }

    if ($("#inactive").length) {
        Materialize.toast("Le contenu que vous lisez est archivé. Ce module n'est probablement plus enseigné à l'ENSAPLV.", 10000);
    }

});
