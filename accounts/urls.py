from django.urls import path
from . import views

print(views)

urlpatterns = [
    path('acconts/', views.home, name='home')
]