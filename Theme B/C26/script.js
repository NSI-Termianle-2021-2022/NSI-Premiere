function test(){
    let game =  document.getElementById("game");
    let ctx = game.getContext("2d")
    ctx.fillStyle = "#ddd"
    ctx.fillRect(0, 0, 50, 50)
    console.log(ctx);
}


function init() {
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
    }
}