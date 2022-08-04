from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('',views.home,name="home"),
    path('debug/',views.debug,name="debug"),
    path('borrow/<int:book_id>',views.borrow,name="borrow"),
    path('sections/',views.sections,name="sections"),
    path('sections/sect/<int:dept>',views.sect,name="sect"),
    path('token/<int:book_id>',views.token,name='token')
    
]