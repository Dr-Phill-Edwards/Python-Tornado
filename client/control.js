function onlogin() {
    const url = "http://localhost:8888/login";
    fetch(url, {
        method : "POST",
        mode: 'cors',
        body: new URLSearchParams(new FormData(document.getElementById("loginform"))),
    })
    .then((response) => {
        return response.text();
    })
    .then(data => {
        document.getElementById('welcome').innerHTML = data;
    })
    .catch(function(error) {
        alert("Error " + error);
    });
}


var websocket = null;
var timer = null;
var counter = 1;
function ontimer() {
    var button = document.getElementById('timer');
    if (button.value == 'Start') {
        document.getElementById('messages').innerHTML = 'Messages\n';
        button.value = 'Stop';
        websocket = new WebSocket('ws://localhost:8888/wsmessage');
        websocket.onmessage = function(event) {
            document.getElementById('messages').innerHTML += event.data + '\n';
        }
        timer = setInterval(function() {
            websocket.send("Chat " + counter);
            counter++;
        }, 2000);
    } else {
        clearInterval(timer);
        websocket.close();
        button.value = 'Start';
        counter = 1;
    }
}