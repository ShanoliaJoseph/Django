from django.urls import path
from .import views

urlpatterns = [
    path("",views.Index,name='Index'),
    path("signin",views.signin,name="signin"),
    path("signup",views.signup,name="signup"),
    path("signout",views.SignOut,name="signout"),
  
   
]
