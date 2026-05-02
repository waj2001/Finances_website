from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
]



urlpatterns = [
   # path("sign_in/",views.signin),
   path("",views.home,name="home"),
   # path("sign_up/",views.signup),
   # path("sign_out/",views.signout),
   path("calc/",views.calculation),
   path("calc/add",views.add),
   path("calc/sub",views.sub),
   path("calc/mult",views.mult),
   path("calc/div",views.div),
   path("calc/home",views.home),

   path("signin/", views.login_view, name="signin"),

   path("signup/", views.signup_view,name="signup"),
   path("signout/", views.signout, name="signout"),
   path("bank/",views.banker)

]