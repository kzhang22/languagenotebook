# pages/urls.py
from django.urls import path
from django.conf.urls import url
from .views import home, signup


urlpatterns = [
    url(r'^signup/', signup, name="signup"),
    url(r'^home/', home, name="home"),
]