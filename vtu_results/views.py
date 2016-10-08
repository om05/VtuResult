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
        # whenever a user enters a usn from the front end and submit the form it comes to this function 
        # since we use post parameter , we need to get the values of those parameter which are  usn and semester 
	if request.method == "POST":
		try:
			usn = request.POST['usn']
			sem = request.POST['sem']
		except KeyError:
			return HttpResponse("wrong way to reach here please go back to the home page")	
		else:
                        # we call get_results_from_dynamodb to connect to dynamodb and get the results stored in it
			results = get_results_from_dynamodb(usn,sem)
			if results:
                                # if no results are found the results variable will be empty 
				return HttpResponse(results)
			else:
                                # when we do not have results in dynamodb u need to check the vtu website if results 
                                # are available if so then display those results and store vtu results in dynamodb
                                # the scraper code is der with u rite ? u need to make use of it to connect to results.vtu and get the results 
                                # (assigned to omkar)
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
