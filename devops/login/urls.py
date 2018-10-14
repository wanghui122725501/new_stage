from django.conf.urls import url,include
from .views import login
urlpatterns = [
    url(r'^$',login,name='login')
]