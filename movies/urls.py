from django.conf.urls import url

from movies import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
