from django.contrib import admin
from django.urls import path
from mysite.views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
]