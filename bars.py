import json


def load_data(filepath):
    with open(filepath) as loads:
        data = json.load(loads)
        return data


def get_biggest_bar(data):
    big = sorted(data, key=lambda k: k['SeatsCount'], reverse=True)
    return big[0]['Name']


def get_smallest_bar(data):
    small = sorted(data, key=lambda k: k['SeatsCount'])
    return small[0]['Name']


def get_closest_bar(data, longitude, latitude):
    for bar in data:
        #closer distance: sqrt((x2-x1)^2+(y2-y1)^2)
        distance =(
        ((float(bar['Longitude_WGS84'])-longitude)**2+
        (float(bar['Latitude_WGS84'])-latitude)**2)**0.5
        )
        #add to bars data distance_key. Lower key - closest
        bar['distance_key']=distance
    closest = sorted(data, key=lambda k: k['distance_key'])
    return closest[0] ['Name']


if __name__ == '__main__':
    
   data=load_data('databars.json')
    big=get_biggest_bar(data)
    small=get_smallest_bar(data)
    latitude = float(input('Широта '))
    longitude = float(input('Долгота '))
    closest=get_closest_bar(data, longitude, latitude)
    print ('Наибольший ',big,'\nНаименьший ',small,'\nБлижайший ',closest)
