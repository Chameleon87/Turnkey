from django.shortcuts import render_to_response
from django.template import RequestContext, Context
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms import ModelForm
from settings import MEDIA_URL
from gallery.models import *
from gallery.forms import ContactForm
    

def index(request):
    return render_to_response('index.html', RequestContext(request))

def customhomes(request):
    return render_to_response('customhomes.html', RequestContext(request))

def roofing(request):
    return render_to_response('roofing.html', RequestContext(request))

def newconstruction(request):
    return render_to_response('newconstruction.html', RequestContext(request))

def remodeling(request):
    return render_to_response('remodeling.html', RequestContext(request))

def concrete(request):
    return render_to_response('concrete.html', RequestContext(request))

def snowremoval(request):
    return render_to_response('snowremoval.html', RequestContext(request))

def gallery(request):
    albums = Album.objects.all()
    if not request.user.is_authenticated():
        albums = albums.filter(public=True)

    paginator = Paginator(albums, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    for album in albums.object_list:
        album.images = album.image_set.all()[:4]

    return render_to_response("gallery.html", dict(albums=albums, user=request.user,
        media_url=MEDIA_URL))

def album(request, pk):
    """Album listing."""
    album = Album.objects.get(pk=pk)
    if not album.public and not request.user.is_authenticated():
        return HttpResponse("Error: you need to be logged in to view this album.")

    images = album.image_set.all()
    paginator = Paginator(images, 30)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        images = paginator.page(page)
    except (InvalidPage, EmptyPage):
        images = paginator.page(paginator.num_pages)

    return render_to_response("album.html", dict(album=album, images=images, user=request.user,
        media_url=MEDIA_URL))

def contact(request):
    if request.POST:
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                send_mail(form.cleaned_data['subject'] + ' ' + form.cleaned_data['type_of_work'], form.cleaned_data['message'], 
                          form.cleaned_data['email'], ['jess@turnkeycc.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('thankyou.html')
        else:
            return render_to_response('contact.html', {'form': form})
    else:
        return render_to_response('contact.html', {'form': ContactForm()},
            RequestContext(request))

def thankyou(request):
    return render_to_response('thankyou.html', RequestContext(request))

def thankyou(request):
		return render_to_response('thankyou.html')
