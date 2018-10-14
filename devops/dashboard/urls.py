from django.conf.urls import url,include
from .views import index,index1
urlpatterns = [
    url(r'^$',index1,name='index1')
]