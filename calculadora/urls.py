"""calculadora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import index
from django.contrib import admin
from django.urls import path, include
from fit.views import *
from django.conf.urls.static import static
from django.conf import settings
from fit import views
from django.contrib.auth import views as auth_views 
from fit.views import UsuarioCreate,PerfilUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('login/', auth_views.LoginView.as_view(
        template_name = "login.html"
    ),name="login"),
    path('login/calculadora/add',add,name="add"),
    path('calculadora/add',add,name="add"),
    path('user/',user,name="user"),
    #path('signup/',signup,name="signup"),
    path('calculadora/',calculadora,name="calculadora"),
    path('blog/',blog,name="blog"),
    path('sobrenos/',sobrenos,name="sobrenos"),
    path('posts/<int:post_id>',views.postagemblog),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('logout/', auth_views.LogoutView.as_view(),name="logout"),
    path('registrar/', UsuarioCreate.as_view(),name="registrar"),
    path('atualizar/', PerfilUpdate.as_view(),name="atualizar"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
