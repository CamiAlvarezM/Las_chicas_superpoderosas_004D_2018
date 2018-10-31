from django.urls import path
from . import views
from blog.views import SignUpView, BienvenidaView, SignInView, SignOutView
from django.conf.urls import * 
from django.conf import settings
from django.contrib import admin
from django.views.generic import RedirectView
from django.contrib.auth.views import ( 
PasswordResetView, 
PasswordResetConfirmView, 
PasswordResetDoneView, 
PasswordResetCompleteView, 
PasswordChangeView, 
PasswordChangeDoneView, 
)
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('index', views.index, name='index'),
    path('galeria', views.galeria, name='galeria'),
    path('admin/blog/Formulario/add/', views.new_perro, name='new_perro'),
    path('admin/blog/Formulario/<int:pk>/change/', views.new_perro, name='new_perro'),
    path('password-reset',PasswordResetView.as_view(), name='password_reset'),

    url(r'^$', BienvenidaView.as_view(), name='bienvenida'),
    url(r'^registrate/$', SignUpView.as_view(), name='sign_up'),
    url(r'^incia-sesion/$', SignInView.as_view(), name='sign_in'),
    url(r'^cerrar-sesion/$', SignOutView.as_view(), name='sign_out'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),

   
]    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)