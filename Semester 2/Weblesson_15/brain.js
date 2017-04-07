function shapes(){
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    var g = canvas.createLinearGradient(10, 10 ,100, 200);
    g.addColorStop(0, "blue";
    g.addColorStop(1,"red");
    
    canvas.fillRect(10, 10, 100, 200);
}

window.addEventListener("load", shapes, false);