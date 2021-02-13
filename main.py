import flickrapi
import json

api_key = u'b766ae533b2843f748b174f53885eee4'
api_secret = u'ac3884caa9690723'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
photos = flickr.photos.search(per_page='100', tags='Finland,Suomi', has_geo=1)
parsed = json.loads(photos.decode('utf-8'))

## 6242 pages, 10 photos per page
## 50932, 10p/p

for item in parsed['photos']['photo']:
    print(item['title'])
id = parsed['photos']['photo'][0]['id']
geo = flickr.do_flickr_call('flickr.photos.geo.getLocation', photo_id=id)
print(json.loads(geo.decode('utf-8')))
