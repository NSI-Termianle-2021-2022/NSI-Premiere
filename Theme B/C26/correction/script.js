// Notez qu'en JavaScript (JS), on doit finir ses lignes avec des ";", sinon
// on peut avoir des problèmes...

// Cette fonction est appelée à chaque clic sur le bouton test
function test() {
    // En JS, on crée des variables avec "let" (pour des variables qui peuvent
    // changer avec déclaration), et "const" (pour des variables qui ne sont pas
    // censées bouger)
    let game = document.getElementById("game");
    let ctx = game.getContext("2d");

    // On décide de colorier nos rectangles en gris...
    ctx.fillStyle = "#ddd";
    // ...et on crée un rectangle de 5 px sur 5 px - càd un carré :)
    ctx.fillRect(0, 0, 5, 5);

    // On signale dans la console qu'on est bien passé dans cette fonction
    console.log("test");
    console.log(ctx);
    // Et comme ça c'est encore plus clair
    alert("I was here!");
}

function mystere(e) {
    // Que fait cette ligne ? Décommentez-la pour voir...
    e.preventDefault();
}

// Cette fonction est appelée à chaque clic sur le bouton init
function init() {
    document.onkeydown = (e) => {
      // switch est un if sophistiqué : si le code de l'événement est "ArrowUp"...
      // ...sinon dans le cas où c'est ArrowDown... etc.
      switch (e.code) {
        case "ArrowUp":
            console.log("En haut");
            break;

        case "ArrowDown":
            console.log("En bas");
            break;

        case "ArrowLeft":
            console.log("À gauche");
            break;

        case "ArrowRight":
            console.log("À droite");
            break;

        // Notez le nom de la clé : "Space"
        case "Space":
            console.log("Ces soirées-là, anhan, anhan");
            break;

        // Notez le nom de la clé : "KeyS", les autres lettres sont identiques
       case "KeyS":
            console.log("On drague, on branche, toi-même tu sais pourquoi");
            break;

        default:
          console.log(e);
      }
      mystere(e);
    };
}
