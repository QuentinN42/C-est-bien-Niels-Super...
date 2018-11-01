function changeHeight()
{
    var w = document.documentElement.clientWidth;
    var maxh = 3648*w/5472
    if(document.documentElement.clientHeight > maxh)
    {
        document.getElementById("main").style.height = maxh+"px";
    }
    else
    {
        document.getElementById("main").style.height = document.documentElement.clientHeight+"px";
    }
};

function hidemain()
{
    document.getElementById(ID).style.display = "None";
}
