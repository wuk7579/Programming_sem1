function validate() {
    var x = document.forms.input.username.value;
    var y = document.forms.input.password.value;
    var passnum = y;
    var atpos = x.indexOf("@");
    var dotpos = x.lastIndexOf(".");

    if ((atpos < 1 || dotpos < atpos+2 || atpos + 2 >x.length) && passnum.length < 6)
        alert("You do not have a valid email address and your passsword does not meetthe minimum requirements");

    else{
        if (atpos < 1 || dotpos < atpos+2 || atpos + 2 >x.length)
            alert("This is not a valid email address!!!!");
        else if (passnum.length < 6)
            alert("Your password does not meet the minimum requirements");
        else
            alert("success!!");}

}
