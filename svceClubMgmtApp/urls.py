from django.urls import path

from . import views
app_name='svceClubMgmtApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.signin,name='signin'),
    path('register',views.signup,name='register'),
    path('logout',views.signout,name='logout'),
    path('club/<str:nm>',views.club,name='clubPage'),
    path('president/<str:nm>',views.club,name='presidenthome'),
    path('president/<str:nm>/e_a_r',views.actrec,name='enable_actively_recruit'),
    path('president/<str:nm>/e_a_r',views.actrec,name='disable_actively_recruit'),
    path('club/<str:nm>/registration',views.register,name='recruit'),
]