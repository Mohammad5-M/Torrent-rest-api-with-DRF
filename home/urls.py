from django.urls import path ,re_path
from home.views import *
urlpatterns = [
    path('', Homeview.as_view(),name='homeview'),
    path('register/', RegisterView.as_view(),name='registerView'),

]
