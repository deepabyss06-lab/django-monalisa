from django.urls import path
from courseapp.views import dj_view
urlpatterns=[
    path('dj/',dj_view,name="dj_view"),
]

