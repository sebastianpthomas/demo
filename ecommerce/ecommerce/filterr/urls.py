from django.urls import path

from . import views

app_name='filterr'

urlpatterns = [

    path('filter/',views.sort_low_to_high,name='sort_low_to_high'),

]