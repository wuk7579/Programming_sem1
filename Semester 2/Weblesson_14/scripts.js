function validate() {
    var x = document.forms.input.username.value;
    var y = document.forms.input.password.value;
    var passnum = y
    var atpos = x.indexOf("@");
    var dotpos = x.lastIndexOf(".")

    if(atpos < 1 || dotpos < atpos+2 || atpos + 2 >x.length)
        alert("This is not a valid email address!!!!")
    if(passnum < 6)
        alert("Your password does not meet the minimum requirements")
    else
        alert("success!!")
}
