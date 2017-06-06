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
    var pic = '<img id = "pikachu" src = http://cdn.bulbagarden.net/upload/thumb/0/0d/025Pikachu.png/250px-025Pikachu.png>
}