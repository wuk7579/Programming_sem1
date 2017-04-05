function validate() {
    var x = document.forms.input.username.value;
    var atpos = x.indexOf("@");
    var dotpos = x.lastIndexOf(".")

    if(atpos < 1 || dotpos < atpos+2 || atpos + 2 >x.length)
        alert("This is not a valid email address!!!!")
    else
        alert("success!!")
}
