function shapes(){
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    var g = canvas.createLinearGradient(10, 10, 700, 520);
    g.addColorStop(0, "blue");
    g.addColorStop(0.3, "white");
    g.addColorStop(0.6, "yellow");
    canvas.fillStyle = g;
    canvas.beginPath();
    canvas.moveTo(200, 0);
    canvas.lineTo(170, 130);
    canvas.lineTo(50, 50);
    canvas.lineTo(130, 170);
    canvas.lineTo(0, 200);
    canvas.lineTo(130, 230);
    canvas.lineTo(50, 350);
    canvas.lineTo(170, 270);
    canvas.lineTo(200, 400);
    canvas.lineTo(230, 270);
    canvas.lineTo(350, 350);
    canvas.lineTo(270, 230);
    canvas.lineTo(400, 200);
    canvas.lineTo(270, 170);
    canvas.lineTo(350, 50);
    canvas.lineTo(230, 130);
    canvas.closePath();
    canvas.fill();
}
window.addEventListener("load", shapes, false);