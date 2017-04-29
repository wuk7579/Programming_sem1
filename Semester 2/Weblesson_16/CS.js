function mouse(){
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    window.addEventListener("mousemove", icon, false);
}
function icon(e){
    canvas.clearRect(0, 0, 1000, 1000);
    var xPos = e.clientX;
    var yPos = e.clientY;
    var pic = new Image();
    pic.src = "http://images.hellokids.com/_uploads/_tiny_galerie/20131042/vign-pikachu-fey_w3g.jpg";
    canvas.drawImage(pic, xPos, yPos, 200, 200);
}
window.addEventListener("load", mouse, false);


