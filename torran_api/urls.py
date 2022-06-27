from django.urls import path ,re_path
from torran_api.views import *
urlpatterns = [
    path('', APIV.as_view(),name='mainapi'),
    path('add/', CAPIV.as_view()),
    path('update/<int:id>', UAPIV.as_view()),
    # re_path(r'^api/(?P<id>[0-9]{4})$', APIV.as_view()),

]
