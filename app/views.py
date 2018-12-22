"""
Definition of views.
"""

from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import *

def artistcreate(request):
    if request.method == "GET":
        form = ArtistForm()
        return render(request, 'app/create.html',{'form':form})
    elif request.method =="POST":
        form = ArtistForm(request.POST)
        form.save()
        return HttpResponseRedirect('/artists')
        
def artists(request):
    artists = Artist.objects.all()
    return render(request,'app/artists.html',{'artists':artists})

def artistdetails(request, id):
    artist = Artist.objects.get(pk = id)
    return render(request,'app/artistdetails.html',{'artist':artist})

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
