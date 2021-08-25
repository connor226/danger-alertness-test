const hitbox = document.getElementById("hit-box");
const video = document.getElementById("video-box");
const button = document.getElementById("play-button");
const container = document.getElementById("video-container");
let timestamp = [];
let placemark = [];
video.addEventListener("ended", () => {
    const form = document.getElementById("req-data");
    let time = document.createElement("input"); //prepare a new input DOM element
    let place = document.createElement("input");
    time.setAttribute("name", "time"); //set the param name
    place.setAttribute("name", "place");
    time.setAttribute("value", timestamp);//set the value
    place.setAttribute("value", placemark);
    form.appendChild(time);//append the input to the form
    form.appendChild(place);
    form.submit();//send with added input
})
button.addEventListener("click", () => {
    video.play();
    container.removeChild(button);
})
function omg(grid){
    timestamp.push(video.currentTime);
    placemark.push(grid.id);
}