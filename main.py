import flickrapi
import json

api_key = u'b766ae533b2843f748b174f53885eee4'
api_secret = u'ac3884caa9690723'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='json')
photos = flickr.photos.search(tags='Tampere', per_page='10')

parsed = json.loads(photos.decode('utf-8'))
print(parsed)
