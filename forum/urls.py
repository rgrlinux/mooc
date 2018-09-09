from django.urls import path
from . import views as v

app_name = 'forum'

urlpatterns = [
    path('', v.index, name='index'),
    path('tag/<str:tag>', v.index, name='index_tagged'),
    path('respostas/<int:pk>/naocorreta/', v.ReplyCorrectView.as_view(), name='reply_incorrect'),
    path('respostas/<int:pk>/correta/', v.ReplyCorrectView.as_view(correct=True), name='reply_correct'),

    path('topico/<str:slug>', v.thread, name='thread'),
]
