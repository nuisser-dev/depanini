
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home_page'),
    path('login', views.login,name='login'),
       path('dashboard/<int:id>', views.ds_dashboard,name='dashboard'),
        path('sgin_up_ds', views.sgin_up_ds,name='sgin_up_ds'),
        path('sgin_up_de', views.sgin_up_de,name='sgin_up_de'),
        path('loginde', views.loginDE,name='loginde'),
        path('cv/<int:id>', views.cv,name='cv'),
        path('dash_de/<int:id>', views.dash_de,name='dash_de'),
         path('ooffer/<int:id>', views.ooffer,name='ooffer'),
]
