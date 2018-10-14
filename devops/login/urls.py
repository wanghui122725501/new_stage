from django.conf.urls import url,include
from .views import loginView
urlpatterns = [
    url(r'^$',loginView,name='loginView')
]