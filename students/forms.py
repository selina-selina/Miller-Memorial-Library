from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UsernameField 
from django.contrib.auth.models import User
from django import forms
from .models import Department

def getDepartmentsList():
    departments_obj = Department.objects.all()
    departments_list = list(departments_obj)
    depts = []
    for x in range(len(departments_list)):
        department = (x,str(departments_list[x]))
        depts.append(department)
    return depts
    
depts = getDepartmentsList()
# CHOICES = {
#       (1, 'Orange'),
#       (2, 'Mango'),
#       (3, 'Strawberries'),
#       (4, 'Grapes'),
      
# }

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Student Resister ID",widget=forms.TextInput(attrs={'placeholder':'Student ID'}))
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder':'1901..@mcc.edu.in'}))
    department = forms.ChoiceField(choices = depts)
    class Meta():
        model = User
        fields = ["username","email","department","password1","password2"]

# class loginform(AuthenticationForm):
#         Studentid = UsernameField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Student ID', 'id': 'hello'}))
#         password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'password',
#             'id': 'hi',
#         }))
        
# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)

#     Studentid = UsernameField(widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Student ID', 'id': 'hello'}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'form-control',
#             'placeholder': 'password',
#             'id': 'hi',
#         }
# ))