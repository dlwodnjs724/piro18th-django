from django.urls import path

from users import views

urlpatterns = [
    path('', views.index),
    path('hello/', views.hello),
    path('<int:pk>/', views.user_detail),
]
