from django.shortcuts import render
from .models import Counter, File, Photo, Video


def main(request):
    return render(request, 'main/about.html')


def achievements(request):
    cs = Counter.objects.all().order_by('id')
    return render(request, 'main/achievements.html', {'cs': cs})


def photos(request):
    ps = Photo.objects.all().order_by('id')
    return render(request, 'main/photos.html', {'ps': ps})


def videos(request):
    vs = Video.objects.all().order_by('id')
    return render(request, 'main/videos.html', {'vs': vs})


def files(request):
    fs = File.objects.all().order_by('id')
    return render(request, 'main/files.html', {'fs': fs})


def contacts(request):
    return render(request, 'main/contacts.html')
