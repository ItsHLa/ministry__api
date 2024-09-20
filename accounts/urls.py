from django.urls import path

from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='sign_up'),
    path('login/', views.login, name='login'), ## login => TokenObtainPairView
    path('logout/', views.logout, name='logout'),
]