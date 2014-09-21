import json
import random

from django.shortcuts import render
from django.http import HttpResponse
from masays.models import Wisdom

# Create your views here.

def index(request):
	return web(request)

def mobile(request):
	wisdom = random.choice(Wisdom.objects.all())
	return HttpResponse(json.dumps({'pub_date': wisdom.pub_date.strftime("%d/%m/%Y %H:%M:%S"), 'content': wisdom.wisdom_text}))

def web(request):
	wisdom = random.choice(Wisdom.objects.all())
	context = {'wisdom': wisdom}
	return render(request, 'masays/index.html', context)
