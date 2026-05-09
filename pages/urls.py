from django.urls import path
from.views import HomeView
from.views import AboutView

urlpatterns = [
    path('', HomeView.as_view(), name =''),
    path('', AboutView.as_view(), name ='')
    
]