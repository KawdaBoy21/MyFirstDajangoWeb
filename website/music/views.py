from django.http import HttpResponse
from .models import Album
# Create your views here.


def index(request):

    all_albums = Album.objects.all()

    for album in all_albums:
        html = ''
        url = '/music/' + str(album.id) + '/'
        html += '<p><a href="' + url + '">' + album.album_title + '</a><p>'
        print(url)
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h1>Album id is: " + str(album_id)+"</h1>")
