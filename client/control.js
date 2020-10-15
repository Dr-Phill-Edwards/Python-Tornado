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

var timer = null;
var counter = 1;
function ontimer() {
    var button = document.getElementById('timer');
    if (button.value == 'Start') {
        document.getElementById('messages').innerHTML = 'Messages Poo\n';
        button.value = 'Stop';
        timer = setInterval(function() {
            document.getElementById('messages').innerHTML += 'Message ' + counter++ + '\n';
        }, 2000);
    } else {
        clearInterval(timer);
        button.value = 'Start';
        counter = 1;
    }
}