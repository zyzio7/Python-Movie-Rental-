from django.core import serializers
from django.shortcuts import render

from .models import Movie


# Create your views here.
def home(request):
    return render(request, "home.html", {'movies': Movie.objects.all()})


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def moviedetails(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "moviedetails.html", {"movie": movie})


def cart(request):
    movie_list = request.session.get("movie")
    # if movie_list is None:
    #     movie_list = [movie]
    # else:
    #     movie_list.append(movie)
    # request.session["movie"] = movie_list
    return render(request, "cart.html", {"movies": movie_list})