from django.urls import path
from . import views as v

app_name = 'forum'

urlpatterns = [
    path('', v.index, name='index'),
    ]