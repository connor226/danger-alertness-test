const hitbox = document.getElementById("hit-box");
const video = document.getElementById("video-box");
const button = document.getElementById("play-button");
const container = document.getElementById("video-container");
let timestamp = [];
hitbox.addEventListener("mousedown", (event) => {
    event.preventDefault();
    hitbox.style.background = "red";
    timestamp.push(video.currentTime);
})
hitbox.addEventListener("mouseup", () => {
    hitbox.style.background = "yellowgreen";
})
video.addEventListener("ended", () => {
    button.disabled = false;
})
button.addEventListener("click", () => {
    /*
    const form = document.getElementById("req-data");
    let data = document.createElement("input"); //prepare a new input DOM element
    data.setAttribute("name", "data"); //set the param name
    data.setAttribute("value", timestamp);//set the value
    form.appendChild(data);//append the input to the form
    console.log(form);
    form.submit();//send with added input
    */
    video.play();
    container.removeChild(button);
})