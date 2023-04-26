"""mywork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from someapp import views
from library import views

# library url
urlpatterns = [
    
    
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('catalog/',views.index, name ='index'),
    path('books/', views.BookListView.as_view() , name = 'books'),
    path('book/<int:pk>',views.BookDetailView.as_view(template_name = 'book_detail.html'),name='book-detail'),
    path('author/',views.AuthorListView.as_view(), name = 'author'),
    path('author/<int:pk>',views.AuthorDetailView.as_view(template_name = 'author_detail.html'), name= 'author-detail'),
    path('mybooks/',views.LoanedBooksByUserListView.as_view(),name='my-borrowed'),

    path('someapp/',views.index1, name="index1"),
    path('someapp/generator/', views.generator, name='generator'),
    path('someapp/password/', views.password, name='password'),
    path('someapp/lottery/', views.lottery, name="lottery"),
    path('someapp/bmi/', views.bmi, name='bmi'),
    path('someapp/gym/', views.gym, name='gym'),
    path('someapp/gym1/', views.gym1, name='gym1'),
    
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
    
]

 #someapp url

    


    # path('admin/', admin.site.urls),
    # path('register/', views.register, name='register'),
    # path('todolist/', views.todolist, name = "todolist"),
    # path('', views.user_login, name="login"),
    # path('logout/', views.user_logout, name='logout'),
    # path('view/<int:todo_id>',views.viewtodo,name="viewtodo"),
    # path('create/', views.createtodo, name="createtodo"),
    # path('view/<int:todo_id>/complete', views.completetodo, name="completetodo"),
    # path('view/<int:todo_id>/delete', views.deletetodo, name="deletetodo"),
    # path('complete/', views.completed, name="completed"),

    
    # path('listall/', views.listall, name = "listall"),
    # path('insert/', views.insert),
    # path('modify/', views.modify),
    # path('delete/', views.delete),




