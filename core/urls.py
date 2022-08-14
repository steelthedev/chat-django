from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.frontpage, name="front"),
    path('signup',views.SignUp, name="signup"),
    path('login',views.Signin, name="login"),
    path('logout',views.Logout_view, name="logout")
]
