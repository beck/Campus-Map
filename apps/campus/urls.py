from django.conf.urls.defaults import *
import settings

urlpatterns = patterns('campus.views',
	url(r'^(\.(?P<format>json|txt))?$', 'home', { 'points' : True }, name="home"),
	url(r'^buildings/(\.(?P<format>json|kml))?$', 'buildings', name="buildings"),
	url(r'^search/(\.(?P<format>json|list))?$', 'search', name="search"),
	url(r'^sidewalks/(\.(?P<format>json|kml|txt))?$', 'sidewalks', name="sidewalks"),
	url(r'^bikeracks/(\.(?P<format>json|txt))?$', 'bikeracks', name="bikeracks"),
	url(r'^emergency-phones/(\.(?P<format>json|txt))?$', 'emergency_phones', name="emergency_phones"),
	url(r'^parking/(\.(?P<format>json|kml|txt))?$', 'parking', name="parking"),
	url(r'^location/(?P<loc>[\w-]+)/([^/]+/)?(\.(?P<format>json|bubble))?$', 'location', name="location"),
	url(r'^regional-campuses/((?P<campus>[\w-]+)/)?(\.(?P<format>json|txt))?$', 'regional_campuses', name="regional"),
)
