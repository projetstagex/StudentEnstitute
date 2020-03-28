from django.urls import path
from .views import *

urlpatterns = [
    path('Enstitute', IndexView.as_view(), name='index'),
    path('Authenticate', Authenticate, name='Authenticate'),
    path('GetStudent', GetStudent, name='GetStudent'),
    path('GetTotalAbsences', GetTotalAbsences, name='GetTotalAbsences'),
    path('GetTotalDelays', GetTotalDelays, name='GetTotalDelays'),
    path('GetModules', GetModules, name='GetModules'),
    path('', AuthenticateView.as_view(), name='auth'),
]