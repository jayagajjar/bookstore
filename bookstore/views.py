import os
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Books

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES',3))
    #return HttpResponse('Hello! ' * times)
    return render(request, "index.html")

def db(request):

    #greeting = Greeting()
    #greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})

def booklist(request):

    books = Books.objects.all()
    return render(request, "booklist.html", {"books": books})

def createbook(request):

    return render(request, "createbook.html")

def insertbook(request):

    booktitle = request.POST.get('booktitle')
    book = Books(title=booktitle,img=booktitle.replace(" ", "") .lower()+'.jpg')
    book.save()
    books = Books.objects.all()
    return render(request, "booklist.html", {"books": books})

def deletebook(request):

    booktitle = request.POST.get('booktitle')
    #return HttpResponse(booktitle)
    Books.objects.filter(title=booktitle).delete()

    books = Books.objects.all()
    return render(request, "booklist.html", {"books": books})


