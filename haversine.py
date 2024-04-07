import math

cities = [
    {'name': 'Ada', 'lat': 40.7695, 'lon': -83.8227 },
    {'name': 'Bellefontaine', 'lat': 40.3612, 'lon': -83.759880},
    {'name': 'Celina', 'lat': 40.54992, 'lon': -84.570808},
    {'name': 'Dayton', 'lat': 39.760979, 'lon': -84.192200},
    {'name': 'Delaware', 'lat': 40.2987, 'lon': -83.0680 },
    {'name': 'Hamilton', 'lat': 39.3995 , 'lon': -84.5613},
    {'name': 'Piqua', 'lat': 40.1448, 'lon': -84.2424},
    {'name': 'Versailles', 'lat': 40.2225, 'lon': -84.4844},
    {'name': 'Xenia', 'lat': 39.6848, 'lon': -83.9297}
    ]

def haversine(user_lat, user_lon, city_lat, city_lon):
    
    #using the haversine formula to calculate the great circle distance between two points
    user_lat_rad = math.radians(user_lat)
    user_lon_rad = math.radians(user_lon)
    city_lat_rad = math.radians(city_lat)
    city_lon_rad = math.radians(city_lon)

    dlon = city_lon_rad - user_lon_rad
    dlat = city_lat_rad - user_lat_rad
    a = math.sin(dlat / 2)**2 + math.cos(user_lat_rad) * math.cos(city_lat_rad) * math.sin(dlon / 2)**2
    c = 2* math.atan2(math.sqrt(a), math.sqrt(1 -a))
    distance = 6371 * c * .621371
    return distance 

def calculate_distances(user_lat, user_lon, cities):
    distances = []
    for city in cities:
        city_name = city['name']
        city_lat = city['lat']
        city_lon = city['lon']
        distance = haversine(user_lat, user_lon, city_lat, city_lon)
        distances.append({'city': city_name, 'distance in miles': distance})
    return distances