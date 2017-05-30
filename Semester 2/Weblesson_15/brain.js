function shapes ()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    var g = canvas.createLinearGradient(0, 0, 400, 400);
    g.addColorStop(0, "red");
    g.addColorStop(1, "blue");
    canvas.fillStyle = g;
    canvas.strokeStyle = "yellow";
    canvas.beginPath();
    canvas.moveTo(200, 0);
    canvas.lineTo(160, 100);
    canvas.lineTo(60, 60);
    canvas.lineTo(100, 160);
    canvas.lineTo(0, 200);
    canvas.lineTo(100, 240);
    canvas.lineTo(60, 340);
    canvas.lineTo(160, 300);
    canvas.lineTo(200, 400);
    canvas.lineTo(240, 300);
    canvas.lineTo(340, 340);
    canvas.lineTo(300, 240);
    canvas.lineTo(400, 200);
    canvas.lineTo(300, 160);
    canvas.lineTo(340, 60);
    canvas.lineTo(240, 100);
    canvas.stroke();
    canvas.fill();
    canvas.closePath();
}

window.addEventListener("load", shapes, false);