document.onkeydown = (e) => {
    switch (e.code) {
        case "Space":
            break;

        case "ArrowUp":
            console.log("haut");
            break;
        
        default:
            console.log(e.code);
    }