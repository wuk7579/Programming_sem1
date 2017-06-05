function drag() {
    clip = document.getElementById("pika");
    leftbox = document.getElementById("left");

    clip.addEventListener("dragstart", startDrag, false);
    clip.addEventListener("dragend", endDrag, false);

    leftbox.addEventListener("dragenter", dragEnter, false);
    leftbox.addEventListener("dragleave", dragLeave, false);
    leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);
}

function startDrag(e) {
    var pic = '<img id = "pika" src = "http://cdn.bulbagarden.net/upload/thumb/0/0d/025Pikachu.png/250px-025Pikachu.png">';
    e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e) {
    e.preventDefault();
    leftbox.style.background = "#00FFFF";
    leftbox.style.border = "5px dashed blue";
}

function dragLeave(e) {
    e.preventDefault();
    leftbox.style.background = "#00FF00";
    leftbox.styleborder = "5px dotted blue";
}

function drop(e) {
    e.preventDefault();
    left.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e) {
    pic = e.target;
    pic.style.visibility = "hidden";
}

window.addEventListener("load", drag, false);