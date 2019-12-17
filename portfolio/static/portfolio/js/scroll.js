document.addEventListener('DOMContentLoaded', function() {
    if (window.matchMedia("(min-width: 768px)").matches) {
        var scrolling = false;
        var target;
        var timeout;

        function scrollX(e) {
            if (e.deltaX == 0) {
                e.preventDefault();

                if (!scrolling) { target = window.scrollX } // Resync with window pos
                target += Math.sign(e.deltaY) * 100;
                window.clearTimeout(timeout); // Flush old timeout
                scrolling = true;
                window.scrollTo({
                    top:  window.scrollY,
                    left: target,
                    behavior: 'smooth'
                });
                timeout = window.setTimeout(function() { scrolling=false; }, 400);
            }
        }

        document.addEventListener('wheel', scrollX, { passive: false });
    }
});