import React from 'react';

const DistanceRoutes = ({ distances, routes }) => {
  return (
    <div>
      <h2>Distances:</h2>
      <ul>
        {distances.map(({ city, distance }) => (
          <li key={city}>
            {city}: {distance} miles
          </li>
        ))}
      </ul>
      <h2>Routes:</h2>
      <ul>
        {Object.entries(routes).map(([city, routeData]) => (
          <li key={city}>
            <p>{city}</p>
            <p>{routeData.summary}</p>
            {/* Display additional route information as needed */}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DistanceRoutes;
