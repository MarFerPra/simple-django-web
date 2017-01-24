from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import json

db_client = settings.DB_CLIENT

db = db_client.db_restaurantes

# Create your views here.

@login_required
def index(request):
    restaurantes = db.restaurants.find()
    all_restaurants = ''
    for res in restaurantes:
        all_restaurants += res.get('name') + ' | '
        all_restaurants += res.get('borough')
        all_restaurants += ' - '
    return HttpResponse(json.dumps(all_restaurants))

@login_required
def test(request):
    return render(request,'test.html', {})

@login_required
def create_restaurant(request):
    if request.method == 'GET':
        return render(request,'restaurantes/create_restaurant.html', {})
    if request.method == 'POST':
        name = request.POST.get('name')
        borough = request.POST.get('borough')
        db.restaurants.insert({'name': name, 'borough': borough})
        return HttpResponse('Restaurant info saved successfully: ' + str(name) + ' '+ str(borough))
