function validate() {
    var x = document.forms.input.username.value;
    var atpos = x.indexOf("@");
    var dotpos = x.lastIndexOf(".");
    if(atpos < 1 || dotpos < atpos+2 || dotpos + 2 > x.length)
        alert("We were unable to process your request."" Please correct the following errors..."
            <br/> "You did not provide a valid email address "
            <br/>"Your password does not meet the minimum requirements");
    else
        alert("success!!!");
}