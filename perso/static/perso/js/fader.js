function fadein (elementId) { // Fondu d'entrée d'un élément
    var elem = document.getElementById (elementId);
    var opac = Number (window.getComputedStyle (elem).getPropertyValue ('opacity')); // On stocke l'opacité CSS initiale
    var id = setInterval (frame, 5); // Boucle d'animation
    function frame () { // Animation
        if (opac < 1.0) {
	        opac += 0.01;
            elem.style.opacity = opac; // Application de l'opacité incrémentée
        }
    }
}

function fadeout (elementId) { // Fondu de sortie d'un élément
    var elem = document.getElementById (elementId);
    var opac = Number (window.getComputedStyle (elem).getPropertyValue ('opacity')); // On stocke l'opacité CSS initiale
    var id = setInterval (frame, 5); // Boucle d'animation
    function frame () { // Animation
        if (opac > 0.0) {
            opac -= 0.01;
            elem.style.opacity = opac; // Application de l'opacité décrémentée
        }
    }
}

function toggleNight () { // Affichage de la carte de nuit
  var elem = document.getElementById ('mainmapnight');
  var opac = Number (window.getComputedStyle (elem).getPropertyValue ('opacity')); // On stocke l'opacité CSS initiale
  if (opac == 0.0) { // Détermine s'il faut afficher ou masquer la carte nocturne
    fadein ('mainmapnight');
  } else {
    fadeout ('mainmapnight');
  }  
}