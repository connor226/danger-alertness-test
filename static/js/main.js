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
    const form = document.getElementById("req-data");
    let data = document.createElement("input"); //prepare a new input DOM element
    data.setAttribute("name", "data"); //set the param name
    data.setAttribute("value", timestamp);//set the value
    form.appendChild(data);//append the input to the form
    form.submit();//send with added input
})
button.addEventListener("click", () => {
    video.play();
    container.removeChild(button);
})