// Get and display current user geolocation.
const output = document.getElementById("out");

getLocation = () => {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        output.innerHTML = "Geolocation is not supported by this browser.";
    }
}

showPosition = (position) => {
    output.innerHTML = "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude;
}