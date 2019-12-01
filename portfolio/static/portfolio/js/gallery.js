document.addEventListener('DOMContentLoaded', function() {
    if (window.matchMedia("(min-width: 768px)").matches) {
        gallery = new Gallery();
    }
});


let Gallery = class {
    constructor(
            galleryId = 'gallery',
            thumbSelector = '#gallery .thumb',
            rowSelector = '#gallery .row') {
        this.gallery = document.getElementById(galleryId);
        this.thumbs = document.querySelectorAll(thumbSelector);
        this.rows = document.querySelectorAll(rowSelector);

        this.draw();
    }

    draw() {
        let me = this;
        let rows_widths = [0, 0];
        
        me.thumbs.forEach(function(thumb) {
            let img = thumb.querySelector('img');
            
            // Hide thumb before it is loaded
            thumb.style.display = 'none';
            img.style.width = 'initial';

            img.addEventListener('load', function() {
                // Reveal image after it is loaded for width calculations
                thumb.style.display = 'initial';
                
                if (rows_widths[0] <= rows_widths[1]) {
                    me.rows[0].appendChild(thumb);
                    rows_widths[0] += thumb.offsetWidth;
                } else {
                    me.rows[1].appendChild(thumb);
                    rows_widths[1] += thumb.offsetWidth;
                }
                
                // Apply styles modifying size after width calculations
                thumb.style.flexGrow = '1';
                img.style.width = '100%';
                me.gallery.style.width = Math.max(...rows_widths) + 'px';
            });
        });
    }
  };
  