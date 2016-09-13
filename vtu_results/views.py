#for every web request the django should return a http response for this reason we import the below lines 
from django.http import HttpResponse

def index(self):
	return HttpResponse("we are building vtu results scraper")