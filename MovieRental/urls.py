"""MovieRental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from movies import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^movie/(?P<movie_id>\d+)/$', views.moviedetails, name='movie'),
    url(r'^movie/title/(?P<movie_title>.+)/$', views.moviedetailsbytitle, name='moviebytitle'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^addtocart/', views.addtocart, name='addtocart'),
    url(r'^deletefromcart/', views.deletefromcart, name='deletefromcart'),
    url(r'^finalize/$', views.finalize, name='finalize'),
    url(r'^register/complete/', views.registration_complete, name='registration_complete'),
    url(r'^register/', views.register, name='register'),
    url(r'^history/', views.history, name='history'),
    url(r'^authors', views.authors, name='authors'),
]
