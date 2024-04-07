import React, { useState } from 'react';
import axios from 'axios';
import LocationInput from './geolocation';
import DistanceRoutes from './DistanceRoutes';

const App = () => {
  const [distances, setDistances] = useState([]);
  const [routes, setRoutes] = useState({});
  const [loading, setLoading] = useState(false);

  const handleLocationSubmit = async ({ latitude, longitude }) => {
    setLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/location', { latitude, longitude });
      setDistances(response.data.distances);
      setRoutes(response.data.routes);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Distance and Route Visualizer</h1>
      <LocationInput onLocationSubmit={handleLocationSubmit} />
      {loading ? (
        <p>Loading...</p>
      ) : (
        <DistanceRoutes distances={distances} routes={routes} />
      )}
    </div>
  );
};

export default App;
