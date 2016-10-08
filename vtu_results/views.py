#for every web request the django should return a http response for this reason we import the below lines 
from django.http import HttpResponse
from django.template import loader

# since we do not want to write our html code inside the view we will write our html in a html file 
# forthis we import django template loader 
from django.http import HttpResponseRedirect
import pdb
def index(request):
        # whenever we create a template html we will obviously need to fill the html will data , in jango we can send those parameter by puttin them in a dictionary called context{}
        context ={}
        pdb.set_trace()
        template=loader.get_template('vtu_results/index.html')
        return HttpResponse(template.render(context,request))
