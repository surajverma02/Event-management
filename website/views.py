from django.shortcuts import render, redirect
from website.models import Event
# Create your views here.

def home(request):
    event = Event.objects.all()

    if request.GET.get('search'):
        
        emps = emps.filter(eventname__icontains = request.GET.get('search'))

    return render (request, 'index.html', {'events':event,})

def add_event(request):

    if request.method=="POST":
        # Data fetching
        eventname  = request.POST.get("eventname")
        date  = request.POST.get("date")
        time  = request.POST.get("time")
        price_started  = request.POST.get("eventprice")
        location  = request.POST.get("location")
        image  = request.POST.get("eventimage")
        

        # create models object and set data
        e = Event()
        e.eventname = eventname
        e.event_date = str(date) + " " + str(time)
        e.price_started = price_started
        e.location = location
        e.image = image
        
        e.save()
        return redirect('/')
    
    return render (request, 'addEvents.html')

def updated(request, id):
    e = Event.objects.get(id = id)

    if e.is_like :
        e.is_like = False
    else :
        e.is_like = True

    e.save()
    return redirect('/')
    

def login_page(request):
    return render (request, 'login.html')

def register_page(request):
    return render (request, 'register.html')