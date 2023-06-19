from . import views
from django.urls import path
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('form', views.form_page, name='form_page'),
    path('logout',views.logout,name='logout')
]