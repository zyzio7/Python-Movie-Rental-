from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf

from movies.forms import RegistrationForm
from .models import Movie, Cart, Rental


# Create your views here.
def home(request):
    if not request.session.exists(request.session.session_key):
        request.session.create()
        request.session['skey'] = request.session.session_key
        cart, created = Cart.objects.get_or_create(session=request.session['skey'])
        cart.session = request.session['skey']
        cart.save()
    return render(request, "home.html", {'movies': Movie.objects.all()})


def login(request):
    return render(request, "login.html")


# def register(request):
#     return render(request, "register.html")


def authors(request):
    return render(request, "authors.html")


def moviedetails(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "moviedetails.html", {"movie": movie})


def moviedetailsbytitle(request, movie_title):
    movie = Movie.objects.get(title=movie_title)
    return render(request, "moviedetails.html", {"movie": movie})


def cart(request):
    cart, created = Cart.objects.get_or_create(session=request.session.get('skey'))
    cart.session = request.session['skey']
    cart.save()
    movie_list = cart.movie.all()
    return render(request, "cart.html", {"movie_list": movie_list, "total_cost": cart.total_cost})


def addtocart(request):
    cart, created = Cart.objects.get_or_create(session=request.session['skey'])
    cart.session = request.session['skey']
    movie_id = request.GET.get('idmovie')
    movie = Movie.objects.get(id=movie_id)
    cart.total_cost = cart.total_cost + movie.price
    cart.save()
    cart.movie.add(movie)
    return render(request, "addtocart.html")


def deletefromcart(request):
    cart, created = Cart.objects.get_or_create(session=request.session['skey'])
    movie_id = request.GET.get('idmovie')
    movie = Movie.objects.get(id=movie_id)
    cart.total_cost = cart.total_cost - movie.price
    cart.save()
    cart.movie.remove(movie)
    return render(request, "deletefromcart.html")


def finalize(request):
    cart = Cart.objects.get(session=request.session['skey'])
    user = request.user
    rental = Rental()
    rental.rent_start_date = datetime.now()
    rental.rent_end_date = datetime.now() + timedelta(days=7)
    rental.total_cost = cart.total_cost
    rental.cart = cart
    rental.user = user
    rental.save()
    return render(request, "finalize.html", {"rental": rental})


def history(request):
    rental_list = Rental.objects.all().filter(user=request.user)
    return render(request, "history.html", {"rental_list": rental_list})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/complete/')

    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render(request, 'registration/registration_form.html', token)


def registration_complete(request):
    return render(request, 'registration/registration_complete.html')
