import React, { useEffect } from 'react';
import getLocation from './geolocation';

function testingComponent() {
    useEffect(() => {
        // calls the getLocation function when the component mounts
        getLocation();
    }, []);

    return (
        <div>
            <h2>test component</h2>

        </div>
    )
       
}

export default testingComponent;