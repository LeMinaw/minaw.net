$( document ).ready(function() {
    play  = $('#play');
    pbar  = document.getElementById('pbar');  
    song  = document.getElementById('audioplayer');
    line1 = $('#line1');
    line2 = $('#line2');
    
	play.on('click', function(e) {
		e.preventDefault();
		if (play.value == "pause") {
		    play.value = "play";
		    song.pause();
		    line1.velocity({ x1:50, y1:0,   x2:275, y2:150, strokeWidth:1.3 });
            line2.velocity({ x1:50, y1:300, x2:275, y2:150, strokeWidth:1.3 });
		} else {
		    play.value = "pause";
		    song.play();
		    line1.velocity({ x1:75,  y1:0, x2:75,  y2:300, strokeWidth:2 });
		    line2.velocity({ x1:225, y1:0, x2:225, y2:300, strokeWidth:2 });
		}
	});
	
	song.addEventListener('timeupdate', function() {
	    elapsedTime = Math.round(song.currentTime);
        if (pbar.getContext) {
            ctx = pbar.getContext("2d");
            ctx.clearRect(0, 0, pbar.clientWidth, pbar.clientHeight);
            ctx.fillStyle = "rgb(255,255,255)";
            fWidth = (elapsedTime / song.duration) * (pbar.clientWidth);
            if (fWidth > 0) {
                ctx.fillRect(0, 0, fWidth, pbar.clientHeight);
            }
        }
	});
    
    pbar.addEventListener("click", function(e) {
        song.currentTime = song.duration * (e.offsetX / pbar.clientWidth);
    }); 
});
