function drag() {
    pikachu = document.getElementById("pikachu");
    leftbox = document.getElementById("leftbox");
    pikachu.addEventListener("dragstart", startDrag, false);
    pikachu.addEventListener("dragend", endDrag, false);
    leftbox.addEventListener("dragenter", dragEnter, false);
    leftbox.addEventListener("dragleave", dragLeave, false);
    leftbox.addEventListener("dragover", function(e) {e.preventDefault()});
    leftbox.addEventListener("drop", drop, false);
}
function startDrag(e) {
    var pic = '<img id = "pikachu" src = "https://www.gannett-cdn.com/-mm-/2f82a576ef5786ba3b027db0c17c35a5d71827f8/c=0-0-475-475&r=x203&c=200x200/local/-/media/2016/07/22/FortMyers/FortMyers/636047918655611038-STGBrd-07-18-2016-Spectrum-1-A001--2016-07-17-IMG-pikachu-1-1-B6F13IBP-L846611140-IMG-pikachu-1-1-B6F13IBP.jpg">'
    e.dataTransfer.setData('picture', pic);
}
function drop(e) {
    e.preventDefault();
    left.innerHTML = e.dataTransfer.getData('picture');
}

function dragEnter(e) {
    e.preventDefault();
    leftbox.style.background = "lightblue";
    leftbox.style.border = "3px solid green"
}
function dragLeave(e) {
    e.preventDefault();
    leftbox.style.background = "yellow";
    leftbox.style.border = "3px solid orange"
}
function endDrag(e) {
    pic = e.target;
    pic.style.visibility = "hidden";
}
window.addEventListener("load", drag, false);