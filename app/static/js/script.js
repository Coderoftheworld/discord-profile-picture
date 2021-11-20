function send() {
    var data = {
        invite: document.getElementById("basic-url").value
    };
    console.log("Sent.")
    fetch("/scrape", {
        headers: {'Content-Type': 'application/json',},
        method: "POST",
        body: JSON.stringify(data)
    })
    .then(res => res.json()).then(data => {
        error_text = document.getElementsByClassName("text-danger").item(0)
        if (data == "Invalid server link") {
            error_text.style.cssText = "padding-top: 14px; display: block; text-align: center;"
        } else if (data == "OK") {
            error_text.style.display = "none"
            downloadLink = document.getElementById("download-link")
            downloadLink.style.display = "unset"
        }
    })

}
