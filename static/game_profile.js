var buttons = document.getElementsByTagName('button')

for (i=0;i<buttons.length;i++) {
    var text = buttons[i].textContent
    var link = "location.href='http://localhost:5000/streamer/" + text + "'"
    buttons[i].setAttribute('onclick', link)
}