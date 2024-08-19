from django.urls import path
from app import views

urlpatterns = [
    path("", views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('profile/<username>/', views.profile, name="profile"),
    path('profileform/', views.profileform, name="profileform"),
    path('logout/', views.signout, name="logout"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path("serviceDetail/<id>/", views.serviceDetail, name="serviceDetail"),
    path("application/<id>/", views.applicationDetail, name="applicationDetail"),
]
