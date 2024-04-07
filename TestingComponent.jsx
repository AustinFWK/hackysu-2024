import React, { useEffect } from 'react';
import getLocation from './geolocation';

function TestingComponent() {
    useEffect(() => {
        // calls the getLocation function when the component mounts
        getLocation();
    }, []);

    return (
        <div>
            <h1>here is where we get your location in latitude and longitude</h1>

        </div>
    )
       
}

export default TestingComponent;