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