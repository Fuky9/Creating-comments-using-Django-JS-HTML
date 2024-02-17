from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.form_view, name='blog'),
]