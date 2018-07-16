from django.urls import path
from django.contrib.auth import views
from . import views as v

app_name = 'accounts'

urlpatterns = [
    path('', v.dashboard,  name='dashboard'),
    path('entrar/', views.login, {'template_name': 'accounts/login.html'}, name='login'),
    path('sair/', views.logout, {'next_page': 'core:home'}, name='logout'),
    path('cadastre-se/', v.register, name='register'),
    path('nova-senha/', v.password_reset, name='password_reset'),
    path('confirmar-nova-senha/<str:key>/', v.password_reset_confirm, name='password_reset_confirm'),
    path('editar/', v.edit, name='edit'),
    path('editar-senha/', v.edit_password, name='edit_password'),

]
