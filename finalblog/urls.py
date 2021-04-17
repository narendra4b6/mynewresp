"""finalblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
from myapp import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register/',views.register.as_view(),name='register'),
    path('accounts/login/',LoginView.as_view(template_name='register/login.html'),name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('accounts/profile/',views.index,name='indexone'),
    path('add/',views.add,name='add'),
    path('drats/',views.drafts,name='drafts'),
    path('posts/<int:pk>/publish/',views.post_publish,name='post_publish'),
    url(r'post_detail/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='post_detail'),
    url(r'post_edit/(?P<pk>\d+)/$',views.PostUpdate.as_view(),name='post_edit'),
    url(r'post_delete/(?P<pk>\d+)/$',views.delete,name="post_delete"),
    url(r'post_comment/(?P<pk>\d+)/$',views.add_comment_post,name="post_comment"),
    url(r'comment_approve/(?P<pk>\d+)/$',views.comment_approve,name="comment_approve"),
    url(r'comment_delete/(?P<pk>\d+)/$',views.comment_delete,name="comment_delete"),


]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
