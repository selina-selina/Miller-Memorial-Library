from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
import datetime
# from .models import Borrow
from students.models import Department,Student

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=350)
    description=models.CharField(max_length=450)
    def __str__(self):
        return self.name
    
class Book(models.Model):
    name=models.CharField(max_length=350)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images/",default="images/default.png")
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,null=True)
    issued=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name  
    
class Borrow(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    token=models.CharField(max_length=10,null=True)
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    created_at=models.DateTimeField( auto_now=True)
    issued=models.BooleanField(default=False)
    issued_at=models.DateTimeField( auto_now=False,null=True,blank=True)
    returned=models.BooleanField(default=False)
    return_date=models.DateTimeField(auto_now=False,auto_created=False,auto_now_add=False,null=True,blank=True)
    
    def __str__(self):
        return f"Borrow Request {self.student} - {self.book} - {self.token} "
        # return "{} - {} book Borrow request".format(self.student,self.book)
    



    def days(self):
        "Returns the no. of days before returning / after return_date."
        if self.issued:
            y,m,d=str(timezone.now().date()).split('-')
            today=datetime.date(int(y),int(m),int(d))
            
            y2,m2,d2=str(self.return_date.date()).split('-')
            lastdate=datetime.date(int(y2),int(m2),int(d2))
            
            print(lastdate-today,lastdate>today)
            if lastdate > today:
                return "{} left".format(str(lastdate-today).split(',')[0])
            else:
                return "{} passed".format(str(today-lastdate).split(',')[0])
        else:
            return ""