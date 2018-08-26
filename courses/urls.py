from django.urls import path
from . import views as v

app_name = 'courses'

urlpatterns = [
    path('', v.index, name='index'),
    path('<slug:slug>/', v.details, name='details'),
    path('<slug:slug>/inscricao/', v.enrollment, name='enrollment'),
    path('<slug:slug>/cancelar-inscricao/', v.undo_enrollment, name='undo_enrollment'),
    path('<slug:slug>/anuncios/<int:pk>/', v.show_announcement, name='show_announcement'),
    path('<slug:slug>/anuncios/', v.announcements, name='announcements'),
    path('<slug:slug>/aulas/', v.lessons, name='lessons'),
    path('<slug:slug>/aulas/<int:pk>/', v.lesson, name='lesson'),
    path('<slug:slug>/materiais/<int:pk>/', v.material, name='material'),
]
