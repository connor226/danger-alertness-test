const hitbox = document.getElementById("hit-box");
const video = document.getElementById("video-box");
const button = document.getElementById("play-button");
const container = document.getElementById("video-container");
let timestamp = [];
let placemarkX = [];
let placemarkY = [];
video.addEventListener("ended", () => {
    const form = document.getElementById("req-data");
    let time = document.createElement("input"); //prepare a new input DOM element
    let placeX = document.createElement("input");
    let placeY = document.createElement("input");
    time.setAttribute("name", "time"); //set the param name
    placeX.setAttribute("name", "placeX");
    placeY.setAttribute("name", "placeY");
    time.setAttribute("value", timestamp);//set the value
    placeX.setAttribute("value", placemarkX);
    placeY.setAttribute("value", placemarkY);
    form.appendChild(time);//append the input to the form
    form.appendChild(placeX);
    form.appendChild(placeY);
    form.submit();//send with added input
})
button.addEventListener("click", () => {
    video.play();
    container.removeChild(button);
    video.addEventListener("click", omg);
})
function omg(event){
    timestamp.push(video.currentTime);
    placemarkX.push(event.clientX/window.innerWidth);
    placemarkY.push(event.clientY/window.innerHeight);
}