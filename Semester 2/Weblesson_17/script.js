function drag() {
    pika = document.getElementById("pikachu");
    leftbox = document.getElementById("leftBox");

    pika.addEventListener("dragstart", startDrag, false);
    pika.addEventListener("dragend", endDrag, false);

    leftbox.addEventListener("dragenter", dragEnter, false);
    leftbox.addEventListener("dragleave", dragLeave, false);
    leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);
}

function startDrag(e) {
    var pic = '<img id = "pikachu" src = http://cdn.bulbagarden.net/upload/thumb/0/0d/025Pikachu.png/250px-025Pikachu.png>'
    e.dataTransfer.setData('picture', pic);
}

function dragEnter(e) {
    e.preventDefault();
    leftbox.style.background = "blue";
    leftbox.style.border = "5px solid yellow";
}
function dragLeave(e) {
    e.preventDefault();
    leftbox.style.background = "blue";
    leftbox.style.border = "5px solid yellow";
}
function drop(e) {
    e.preventDefault();
    leftBox.innerHTML = e.dataTransfer.getData('picture');
}

function endDrag(e) {
    pic = e.target;
    pic.style.visibility = "hidden";
}
window.addEventListener("load", drag, false);