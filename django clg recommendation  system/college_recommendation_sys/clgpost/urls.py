from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from clgpost.views import college ,single_colg
from . import views

urlpatterns = [
 path('college/',college,name="college"),
 
 path('<str:slug>/',single_colg,name="single_colg"),

 


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)