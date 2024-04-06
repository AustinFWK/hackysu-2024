from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/location', methods=['POST'])
def receive_location():
    #extracts the location data from the request
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']

    #we can process the data here but we are printing at the moment
    print(f'Latitude: {latitude}, Longitude: {longitude}')

    #returns a response to allow us to know if it worked
    return jsonify({'message': 'Location received successfully.'}), 200

if __name__ == '__main__':
    app.run(debug=True)