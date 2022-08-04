from django.contrib import admin
from .models import Book,Author,Borrow

# Register your models here.
@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass

@admin.register(Author)
class Adminauthor(admin.ModelAdmin):
    pass

@admin.register(Borrow)
class Borrow(admin.ModelAdmin):
    pass
