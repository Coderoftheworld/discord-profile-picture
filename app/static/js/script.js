function send() {
    var data = {
        invite: document.getElementById("basic-url").value
    };
    console.log("Sent.")
    fetch("/scrape", {
        headers: {'Content-Type': 'application/json',},
        method: "POST",
        body: JSON.stringify(data)
    }).then(res => res.json()).then(data => {
        downloadLink = document.getElementById("download-link")
        downloadLink.style.display = "unset"; downloadLink.href = data; downloadLink.download = "server-icon.png"
    })

}
