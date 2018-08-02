from django.contrib import admin
from django.urls import path
# from django.conf.urls import url, include
# from django.contrib.auth import views as auth_views

# from accounts import views as accounts_views
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
]