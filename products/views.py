from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Farm_produces
from .models import Latest_farm_produces
from .models import Rolgezfarm_services
from .models import Rolgezfarm_contacts
# Create your views here.
def index(request):
    latest = Latest_farm_produces.objects.all()
    homecont = Rolgezfarm_contacts.objects.filter()
    return render(request, 'index.html', {'latest':latest, 'homecont':homecont})
def about(request):
    aboutr = Rolgezfarm_services.objects.filter()
    aboutcont = Rolgezfarm_contacts.objects.filter()
    return render(request, 'about.html', {'aboutr':aboutr, 'aboutcont':aboutcont})
def contact(request):
    contactr = Rolgezfarm_contacts.objects.filter()
    return render(request, 'contact.html', {'contactr':contactr})
def products(request):
    prodcont = Rolgezfarm_contacts.objects.filter()
    prodr = Farm_produces.objects.all()
    return render(request, 'gallery.html', {'prodr':prodr, 'prodcont':prodcont})
