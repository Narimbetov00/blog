from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('new/',views.create_post,name='new_post'),
    path('registration/',views.registration,name="registration"),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    
]