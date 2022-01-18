from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='about'),
    path('achievements/', views.achievements, name='achievements'),
    path('photos/', views.photos, name='photos'),
    path('videos/', views.videos, name='videos'),
    path('files/', views.files, name='files'),
    path('contacts/', views.contacts, name='contacts'),
]
