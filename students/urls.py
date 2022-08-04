from django.contrib.auth import views as v
from django.urls import path,include
from . import views

app_name = 'students'
urlpatterns = [
    # path('',include("django.contrib.auth.urls")),
    path('register',views.register,name='register'),
    path('login/',views.studentlogin,name="login"),
    path('student',views.student,name="student")
]
