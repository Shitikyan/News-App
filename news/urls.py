from django.urls import path
from news import views

urlpatterns = [
    path("", views.home, name='home'),
    path("news/<str:title>", views.news, name="single_news"),
    path("category/<str:name>", views.category, name="single_category"),
    path("newsroom/<str:option>", views.newsroom, name="news room"),
    path("categories/", views.categories, name="categories"),
    path("contact/", views.contact, name="contact"),
]
