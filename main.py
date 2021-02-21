import flickrapi
import json

api_key = u'b766ae533b2843f748b174f53885eee4'
api_secret = u'ac3884caa9690723'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
# Get all pictures from Finland
photos = flickr.photos.search(per_page='100', tags='Finland,Suomi', has_geo=1)
parsed = json.loads(photos.decode('utf-8'))

## 6242 pages, 10 photos per page
## 50932, 10p/p
## id | location | name | tags

for item in parsed['photos']['photo']:
    print(item['title'])
id = parsed['photos']['photo'][0]['id']
geo = flickr.do_flickr_call('flickr.photos.geo.getLocation', photo_id=id)
print(json.loads(geo.decode('utf-8')))


# 50 lat x 50 lon -> at least 500 squares

for lat in range(latidudes):
    for lon in range(longitudes):
        photos = flickr.photos.search(per_page='100', lat=lat, lon=lon, accuracy=10, has_geo=1)
        users_visited = []
        parsed = json.loads(photos.decode('utf-8'))
        id = parsed['photos']['photo'][0]['id']
        geo = flickr.do_flickr_call('flickr.photos.geo.getLocation', photo_id=id)


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

def find_same_users(set1, set2):
    return [user1, user2]

users = len(find_same_users(photos1, photos2))