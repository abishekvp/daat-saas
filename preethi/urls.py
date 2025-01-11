from django.urls import path
from . import views

urlpatterns=[
    path('html/',views.req_obj),
]
