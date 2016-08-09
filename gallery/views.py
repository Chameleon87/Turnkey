from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.forms.widgets import *
from settings import MEDIA_URL
from gallery.models import Album
from gallery.forms import ContactForm


def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def customhomes(request):
    return render(request, 'customhomes.html')


def roofing(request):
    return render(request, 'roofing.html')


def newconstruction(request):
    return render(request, 'newconstruction.html')


def remodeling(request):
    return render(request, 'remodeling.html')


def concrete(request):
    return render(request, 'concrete.html')


def snowremoval(request):
    return render(request, 'snowremoval.html')


def gallery(request):
    albums = Album.objects.all()
    if not request.user.is_authenticated():
        albums = albums.filter(public=True)

    paginator = Paginator(albums, 10)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        albums = paginator.page(page)
    except (InvalidPage, EmptyPage):
        albums = paginator.page(paginator.num_pages)

    for album in albums.object_list:
        album.images = album.image_set.all()[:4]

    return render(request, "gallery.html", dict(albums=albums, user=request.user,
                                                media_url=MEDIA_URL))


def album(request, pk):
    """Album listing."""
    album = Album.objects.get(pk=pk)
    if not album.public and not request.user.is_authenticated():
        return HttpResponse("Error: you need to be logged in to view this album.")

    images = album.image_set.all()
    paginator = Paginator(images, 30)
    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        images = paginator.page(page)
    except (InvalidPage, EmptyPage):
        images = paginator.page(paginator.num_pages)

    return render(request, "album.html", dict(album=album, images=images, user=request.user,
                                              media_url=MEDIA_URL))


def contact(request):
    if request.POST:
        form = ContactForm(request.POST)
    else:
        form = ContactForm()

    if form.is_valid():
        try:
            send_mail(form.cleaned_data['subject'] + ' ' + form.cleaned_data['type_of_work'], form.cleaned_data['message'],
                      form.cleaned_data['email'], ['jess@turnkeycc.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('thankyou.html')
    else:
        return render(request, 'contact.html', {'form': form})


def thankyou(request):
    return render(request, 'thankyou.html')
