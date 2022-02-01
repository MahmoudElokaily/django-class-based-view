from django.urls import path
from . import views

urlpatterns = [
    path('' , views.post_list , name = ""),
    path('postdetails/', views.post_details , name=""),

]