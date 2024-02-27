from django.urls import path
from usermanagement import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]