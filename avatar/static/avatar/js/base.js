$(document).ready(function() {
    $.taconite.debug = true;

    $("#testForm").on("submit", function(e) {
        e.preventDefault();
        $.post("", $("#testForm").serialize()); // Sending form thru AJAX
    });
});
