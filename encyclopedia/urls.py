from django.urls import path
from . import util
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("wiki/?q=<str:entry>", views.search, name="search")
]


#서치 부분 url로 고치려고 하는중#