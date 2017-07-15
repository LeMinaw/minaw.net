function toggleComments(id) {
    $('#' + id).toggle();
}

function toggleMenu() { // TODO: fix
    $('#nav').toggle();
}

function displaySubscribe() {
    $('#subscribeModal').show();
}

function hideModals() {
    $('.w3-modal').hide();
}

$(document).ready(function() {
    if ($('#sucessModal').length) {
        $('#sucessModal').show();
    }
});

$(document).mouseup(function(e) {
    var modal = $('.w3-modal-content');
    if (!modal.is(e.target) && modal.has(e.target).length === 0) {
        hideModals();
    }
});

$('.w3-justify img').not('.comments img').on('click', function() {
    $('#img_fullsize').attr('src', $(this).attr('src'));
    $('#photoModal').show();
});
