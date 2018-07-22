from django.urls import path
from . import views as v

app_name = 'courses'

urlpatterns = [
    path('', v.index, name='index'),
    path('<slug:slug>/', v.details, name='details'),
    path('<slug:slug>/inscricao/', v.enrollment, name='enrollment'),
]
