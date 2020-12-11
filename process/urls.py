from django.urls import path
from process import views


urlpatterns = [
    path('', views.showIndex, name='main_page'),
    path('registration/', views.registration, name='registration'),
    path('user_registration/', views.registration, name='user_registration'),
    path('validation_otp/',  views.validate_otp, name='validate_otp'),
    #otp page
    path('user_otp/', views.userOTP, name='user-otp'),
    # conformation
    path('conformation/', views.conformation, name='conformation'),

    #login
    path('login/', views.login, name='login'),
    #for login check
    path('login_check/', views.login_check, name='login_check'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('logout/',views.logout,name='logout'),

]
