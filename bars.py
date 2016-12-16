import json


def load_data(filepath):
    with open(filepath) as databars_loads:
        bars_data = json.load(databars_loads)
        return bars_data


def get_biggest_bar(data):
    big_bar = max(data, key=lambda k: k['SeatsCount'])
    return big_bar['Name']


def get_smallest_bar(data):
    small_bar = min(data, key=lambda k: k['SeatsCount'])
    return small_bar['Name']


def get_closest_bar(data, longitude, latitude):
    for bar in data:
        # closer distance: sqrt((x2-x1)^2+(y2-y1)^2)
        distance = (
                    ((float(bar['Longitude_WGS84'])-longitude)**2 +
                     (float(bar['Latitude_WGS84'])-latitude)**2)**0.5)
        # add to bars data distance_key. Lower key - closest
        bar['distance_key'] = distance
    closest_bar = min(data, key=lambda k: k['distance_key'])
    return closest_bar['Name']

if __name__ == '__main__':
    file_path = input('Укажите путь к файлу списка баров (json): ')
    bars_data = load_data(file_path)
    big_bar = get_biggest_bar(bars_data)
    small_bar = get_smallest_bar(bars_data)
    my_latitude = float(input('Широта '))
    my_longitude = float(input('Долгота '))
    closest_bar = get_closest_bar(bars_data, my_longitude, my_latitude)
    print(
        'Наибольший бар: ', big_bar, '\nНаименьший бар: ', small_bar,
        '\nБлижайший бар: ', closest_bar)
