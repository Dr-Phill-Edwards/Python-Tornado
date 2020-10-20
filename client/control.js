var accesstoken = null;

function onlogin() {
    const url = "http://localhost:8080/login";
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

var signIn = new OktaSignIn({
    baseUrl: 'https://dev-436256.okta.com',
    clientId: '0oaavsqp2YFRRTL5x5d5',
    authParams: {
        issuer: 'https://dev-436256.okta.com/oauth2/default',
        responseType: ['token', 'id_token']
    }
});

signIn.renderEl({
    el: '#login-container'
}, function success(res) {
    if (res.status === 'SUCCESS') {
        accesstoken = res.tokens.accessToken.accessToken;
        var idtoken = res.tokens.idToken;
        document.getElementById('login-container').innerHTML = "<h3>" + idtoken.claims.email + " Logged In</h3><br/>" + accesstoken;
        document.getElementById('token').value = accesstoken;
    } else {
        alert('fail);')
    }
}, function(error) {
    alert('error ' + error);
});