function sendLocationToBackend(latitude, longitude){
//sends an HTTP POST request to flask backend
    fetch('http://127.0.0.1:5000/api/location', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({latitude, longitude})
    })
    .then(repsonse => {
        if (Response.ok) {
            console.log('you have successfully sent your location to our backend.');

        }
        else {
            console.error('there was an error sending the location');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });

}
//this function actually retrieves the location of the user
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            position => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                sendLocationToBackend(latitude, longitude);
            },
            error => {
                console.error('Geolocation error:', error.message);
            }
        );
    } else {
        console.error('Geolocation is not supported by this browser.');
    }
}
//this exports the users data 
export default getLocation;