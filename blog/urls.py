from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',views.loginpage,name='login'),
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('post/<int:id>/update',views.update_post,name='update_post'),
    path('post/<int:id>/delete',views.delete_post,name='delete_post'),
    path('new/',views.create_post,name='new_post'),
    path('registration/',views.registration,name="registration"),
    path('login/',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    
]