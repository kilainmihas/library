from django.urls import path

from someapp import views

urlpatterns = [
    path("someapp/", views.index,name="index"),
    path('generator/', views.generator, name='generator'),
    path('password/', views.password, name='password'),
    path('lottery/', views.lottery, name="lottery"),
    path('bmi/', views.bmi, name='bmi'),
    path('gym/', views.gym, name='gym'),
    path('gym1/', views.gym1, name='gym1'),
]