from django import db
from django.shortcuts import render
from requests import request
import random

from students.models import Department, Student
from .models import Book,Author, Borrow
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def home(request):
    current_user = request.user
    context ={"user":current_user}
    
    if "usersearch" in request.GET:
        query = request.GET['usersearch']
        u = Book.objects.filter(name__startswith=query).all()
        context['query'] = u
        context['item'] = query
        
    return render(request,'books/home.html', context)

def debug(request):
     #debug start
    booksfromdb = Book.objects.all()
    context = {'books': booksfromdb}
    #debug end
    return render(request,'books/debug.html', context)
@login_required
def borrow(request,book_id):
    book = Book.objects.get(id=book_id)
    context = {'book' : book}
    return render(request,'books/borrow.html',context)


@login_required
def token(request,book_id):
    req_book = Book.objects.get(id=book_id)
    current_user = request.user
    student = Student.objects.get(student_id=current_user)
    
    token = ''
    if request.method == 'POST':
        if req_book.issued == False:
            seq = (1,2,3,4,5,6,7,8,9,0)
            tk = random.sample(seq,5)
            token = int(''.join(str(e) for e in tk))
            print(student)
            
            borrow_req = Borrow(book=req_book,student=student,token=token)
            borrow_req.save()
        return render(request,'books/token.html',{'token':token})
        # return render(request,'books/token.html', )

def sections(request):
    
    # sections = ['Commerce','English','Tamil','History','Political Science','Mathematics','Economic',
    #             'statistics','Public Administration','Social Work','Chemistry','Physics','Botony','Zoology','Physical Education']
    # sfs = ['Journalism','Computer Application','Computer Science','Visual Communication','Psycology']
    
    # lib_sec = ['Reference','Commerce','Visual Communication','Tamil','English','Mathematic','History','Chemistry','Botony',
    #            'Zoology','Economics','Computer Application','Computer Science','Public Administration','Social Work']
    icons = ['fa-solid fa-briefcase','fa-solid fa-clapperboard','fa-solid fa-gopuram','fa-solid fa-archway','fa-solid fa-divide','fa-solid fa-landmark-dome','fa-solid fa-flask','fa-solid fa-seedling','fa-solid fa-frog','fa-solid fa-globe','fa-solid fa-desktop','fa-solid fa-chart-pie','fa-solid fa-users']
    books = Book.objects.all()
    lib_sec = Department.objects.all()
    context = {"sections": lib_sec,"books":books,"icons":icons}
    return render(request,'books/sections.html', context)


def sect(request,dept):
    depart = Department.objects.get(id=dept)
    print(depart.id)
    books = Book.objects.filter(department=depart.id)
    # borrow_list = Borrow.objects.all()
    return render(request,'books/sect.html', {"dept":depart,"books":books,})

