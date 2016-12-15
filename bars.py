import json

def load_data(filepath):
    with open(filepath) as databars_loads:
        bars_data = json.load(databars_loads)
        return bars_data

def get_biggest_bar(data):
    big_bar = sorted(data, key=lambda k: k['SeatsCount'], reverse=True)
    return big_bar[0]['Name']


def get_smallest_bar(data):
    small_bar = sorted(data, key=lambda k: k['SeatsCount'])
    return small_bar[0]['Name']


def get_closest_bar(data, longitude, latitude):
    for bar in data:
        #closer distance: sqrt((x2-x1)^2+(y2-y1)^2)
        distance =(
        ((float(bar['Longitude_WGS84'])-longitude)**2+
        (float(bar['Latitude_WGS84'])-latitude)**2)**0.5
        )
        #add to bars data distance_key. Lower key - closest
        bar['distance_key']=distance
    closest_bar = sorted(data, key=lambda k: k['distance_key'])
    return closest_bar[0] ['Name']

if __name__ == '__main__':
    
    load_data=load_data('databars.json')
    big=get_biggest_bar(load_data)
    small=get_smallest_bar(load_data)
    latitude = float(input('Широта '))
    longitude = float(input('Долгота '))
    closest=get_closest_bar(load_data, longitude, latitude)
    print ('Наибольший бар ',big,'\nНаименьший бар ',small,'\nБлижайший бар',closest)
