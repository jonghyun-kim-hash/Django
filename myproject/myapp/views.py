from django.shortcuts import render, HttpResponse
# import random

topics = [
    {'id': 1, 'title': 'routing', 'body': 'Rounting is ... ' },
    {'id': 2, 'title': 'view', 'body': 'View is ... ' },
    {'id': 3, 'title': 'model', 'body': 'Model is ... ' }
]

# Create your views here. 
def index(request):
    # return HttpResponse('<h2>Random : </h2>' + str(random.random()))
    
    global topics
    return render(request, 'myapp/homepage.html', {'topics': topics})

def create(request):
    return HttpResponse('Create!')

def read(reques, id):
    return HttpResponse('Read! ' + id)