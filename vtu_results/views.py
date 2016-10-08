#for every web request the django should return a http response for this reason we import the below lines 
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from aws_keys import dynamodb
# since we do not want to write our html code inside the view we will write our html in a html file 
# forthis we import django template loader 
from django.http import HttpResponseRedirect
import pdb

def index(request):
        # whenever we create a template html we will obviously need to fill the html will data , in jango we can send those parameter by puttin them in a dictionary called context{}
        context ={}
        template=loader.get_template('results/index.html')
        return HttpResponse(template.render(context,request))

def marks(request):
	if request.method == "POST":
		try:
			usn = request.POST['usn']
			sem = request.POST['sem']
		except KeyError:
			return HttpResponse("wrong way to reach here please go back to the home page")	
		else:
			results = get_results_from_dynamodb(usn,sem)
			if results:
				return HttpResponse(results)
			else:
				return HttpResponse('needs handling')		
	else :
			return HttpResponse("wrong way to reach here please go back to the home page")			

def get_results_from_dynamodb(usn,sem):
	#pdb.set_trace()
	usn_sem = usn+"_"+sem
	dynamodb_object = dynamodb()
	results = dynamodb_object.get_results(usn_sem)
	if results:
		print results
		return results

	else :
		return None