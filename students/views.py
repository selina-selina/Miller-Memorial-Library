from django.shortcuts import render , redirect

from books.models import Book, Borrow
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login
from .models import Department, Student
from django.contrib.auth.models import User



def getDepartmentsList(index):
    dept_query = Department.objects.all()
    dept_list = list(dept_query)
    depts = []
    for x in range(len(dept_list)):
        p = str(dept_list[x])
        depts.append(p)
    return depts[int(index)]

# Create your views here.
def studentlogin(request):
    if request.method == 'POST':
        username = request.POST.get('studentroll')
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
        return redirect("/")
    
    return render(request,'students/login.html' )


def logout(request):
    return render(request,'logged_out.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=request.POST.get('username')
            password= request.POST.get('password2')
            dept= request.POST.get('department')
            print(dept)
            dept_name = getDepartmentsList(dept)
            print(dept_name)
            
            # Querying Department Object
            department = Department.objects.get(name=dept_name)
            print(department)
            current_user = User.objects.get(username=username)
            print(current_user)
            #adding student
            new_student = Student(department=department,student_id=current_user)
            new_student.save()
            new_user = authenticate(username=username,
                                    password=password)
            login(request,new_user)
            return redirect("/")
    else:
        form = RegistrationForm()
        
    return render(request,'students/register.html',{'form': form})

def student(request):
    current_user = request.user
    student = Student.objects.get(student_id=current_user)
    borrwed = Borrow.objects.filter(student=student)
    context = {"user":current_user,"borrowed":borrwed}
    return render(request,'students/student.html', context)