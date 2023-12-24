from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 

from .views import recommend_colleges

urlpatterns = [
 
 path('recommend/', recommend_colleges, name='recommend_colleges'),

 
]