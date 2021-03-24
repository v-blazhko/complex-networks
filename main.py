import flickrapi
import json
import requests
import flickrapi
import pandas as pd
from tqdm import tqdm
from vincenty import vincenty
import matplotlib.pyplot as plt
import time
import numpy as np

api_key = u'b766ae533b2843f748b174f53885eee4'
api_secret = u'ac3884caa9690723'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')

f = open('dataset/raw/veronika_users.csv', 'a')

for row in tqdm(photo_ids[780:38000]):
    photo = flickr.do_flickr_call('flickr.photos.getInfo', photo_id=row)
    parsed = json.loads(photo.decode('utf-8'))
    user = parsed['photo']['owner']['username']
    s = str(row) + ',' + user + '\n'
    f.write(s)
f.close()


min_lat = 59.800
max_lat = 69.910
min_lon = 20.410
max_lon = 30.920

n_lat = 6
n_lon = 4

start_lat = min_lat
start_lon = min_lon

lats = np.arange(min_lat, max_lat, (max_lat - min_lat) / n_lat)
lons = np.arange(min_lon, max_lon, (max_lon - min_lon) / n_lon)

bboxes = []

for i_lat, lat in enumerate(lats):
    for i_lon, lon in enumerate(lons):
        print('\n')
        if i_lon + 1 != n_lon:
            bbox = (lon, lat, lons[i_lon + 1], lats[i_lat + 1])

        else:
            bbox = (lon, lat, max_lon, max_lat)
        print(bbox)
# 50 lat x 50 lon -> at least 500 squares

# for lat in range(latidudes):
#     for lon in range(longitudes):
#         photos = flickr.photos.search(per_page='100', lat=lat, lon=lon, accuracy=10, has_geo=1)
#         users_visited = []
#         parsed = json.loads(photos.decode('utf-8'))
#         id = parsed['photos']['photo'][0]['id']
#         geo = flickr.do_flickr_call('flickr.photos.geo.getLocation', photo_id=id)


# dict = {location: [user1, user2]}

# -> 500 locations
#
# 500 x 500 requests to flickr
#
# dist_between_nodes < 100km
# n_of ppl_visited_both > 2
#
# if (condition):
#     nx.add_edge()

# def find_same_users(set1, set2):
#     return [user1, user2]
#
# users = len(find_same_users(photos1, photos2))