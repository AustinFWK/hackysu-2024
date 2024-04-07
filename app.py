from flask import Flask, request, jsonify
from flask_cors import CORS
from haversine import calculate_distances, haversine, cities
import requests

app = Flask(__name__)
CORS(app)

directions_api_url = "https://maps.googleapis.com/maps/api/directions/json"
api_key="AIzaSyAzacQQZ0v1zUpDwTwdQ5uhbCKZ4Gm3ogI"

@app.route('/api/location', methods=['POST'])
def receive_location():
    data = request.json
    #extracts the location data from the request
    latitude = data['latitude']
    longitude = data['longitude']
    routes = {}

    for city in cities:
        city_name = city['name']
        city_lat = city['lat']
        city_lon = city['lon']

    params = {
        "origin": f"{latitude},{longitude}",
        "destination": f"{city_lat},{city_lon}",
        "key": api_key
    }

    response = requests.get(directions_api_url, params=params)
    route_data = response.json()

    routes[city_name] = route_data
    
    #we can process the data here but we are printing at the moment
    #print(f'Latitude: {latitude}, Longitude: {longitude}')

    #returns a response to allow us to know if it worked
    distances = calculate_distances(latitude, longitude, cities)
    response_data = {"distances": distances, "routes": routes}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)