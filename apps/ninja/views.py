from django.shortcuts import render,redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'activities' not in request.session:
        request.session['activities'] = []
    context = {
        'time': datetime.now()
    }
    return render(request,"ninja/index.html", context)

def process(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if request.POST['building'] == 'farm':
        gold = random.randrange(10,21)
        request.session['gold'] += gold
        request.session['activities'].append("Earned {} gold from the farm)".format(int(gold)))
    elif request.POST['building'] == 'cave':
        gold = random.randrange(5,11)
        request.session['gold'] += gold
        request.session['activities'].append("Earned {} gold from the cave)".format(int(gold)))
    elif request.POST['building'] == 'house':
        gold = random.randrange(2,6)  
        request.session['gold'] += gold
        request.session['activities'].append("Earned {} gold from the house)".format(int(gold)))
    elif request.POST['building'] == 'casino':
        gold = random.randrange(-51,51)
        request.session['gold'] += gold
        request.session['activities'].append("Earned {} gold from the casino)".format(int(gold)))
    return redirect('/home')

def home(request):
    return redirect ('/')




# Create your views here.
