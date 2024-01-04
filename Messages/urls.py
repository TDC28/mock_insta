from . import views
from django.urls import path
urlpatterns = [
    path('messages/', views.messages)

]