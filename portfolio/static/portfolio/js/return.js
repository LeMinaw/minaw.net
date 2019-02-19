var go_back = function(fallback_url=null, timeout=200) {
    window.history.back();

    if (fallback_url != null) {
        window.setTimeout(function() {
            window.location.href = fallback_url;
        }, timeout);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    window.addEventListener('keydown', function(e) {
        
        if (e.key == 'Escape') {
            go_back();
        }
    });

    window.addEventListener('click', function(e) {
        if (!document.getElementById('work').contains(e.target)
                && e.target.tagName.toLowerCase() != 'a') {
            go_back();
        }
    });
});