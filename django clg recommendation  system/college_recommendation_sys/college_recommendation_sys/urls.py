"""
URL configuration for college_recommendation_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include 
from college_recommendation_sys import views

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    # path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('home/',views.home1,name='home'),

    path('about/',views.aboutus ,name='aboutus'),

    path("recommendation/", views.recommendation, name="recommendation"),
    # path("single_deg/", views.single_degree, name="single_deg") ,

    path('feedback/',views.feedback ,name='feedback'),
    path('submit_review/', views.submit_review, name='submit_review'),

 
   
    

    path('degree/',views.degree ,name='degree'),
    path('<str:slug>/',views.single_degree,name="single_deg"),
    
    # path('<str:slug>/',views.single_colg, name="single_colg"),
    path('clgpost/',  include('clgpost.urls')),
    path('recommendation/',include('recommendation.urls'))

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
