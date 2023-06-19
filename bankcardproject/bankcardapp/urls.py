from . import views
from django.urls import path
app_name='bankcardapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services')
]