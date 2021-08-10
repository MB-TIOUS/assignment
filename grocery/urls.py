from django.urls import path
from grocery import views

urlpatterns = [
    path("", views.index,name="login"),
    path("index",views.index,name="index"),
    path("signup",views.signup,name="signup"),
    path("logout",views.logout,name="logout"),
    path('add',views.add_list,name='add_list'),
    path('update/<int:id>',views.update_list,name='update_list'),
    path('view_list',views.view_list,name='view_list'),
    path("list_delete/<int:id>",views.list_delete,name="list_delete"),
]