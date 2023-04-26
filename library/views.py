from msilib.schema import ListView
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.views import generic
from django.contrib import sessions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required
import random
# Create your views here.

def index(request):
    num_books = Book.objects.all().count()
    num_instance = Bookinstance.objects.all().count()
    num_instance_available = Bookinstance.objects.filter(status__exact = 'a').count()
    num_author = Author.objects.all().count()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instance,
        'num_instance_available': num_instance_available,
        'num_authors': num_author,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by =  5
class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)

        return render(request, 'book_detail.html', context={'book':book})


class AuthorListView(generic.ListView):
    model = Author
    template_name = 'author_list.html'
    paginate_by =  5

class AuthorDetailView(generic.DetailView):
    model = Author
    

    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk = primary_key)
        
        return render(request, 'author_detail.html', context = {'author':author})

    

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = Bookinstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return Bookinstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

@login_required
def generator(request):
    return render(request,'generator.html')


@login_required
def password(request):

    if request.GET.get('number-length'):
        length = eval(request.GET.get('number-length'))
    else:
        length = eval(request.GET.get('length'))

    password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters+= list('abcdefghijklmnopqrstuvwxyz'.upper())

    if request.GET.get('number'):
        characters+= list('0123456789')

    if request.GET.get('special'):
        characters+= list('!@#$%^&*()_~')    

    for i in range(length):
        password += random.choice(characters)

    return render(request, 'password.html' , {'password': password})

@login_required
def lottery(request):
    return render(request ,"lottery.html")


@login_required
def bmi(request):
    return render(request ,"bmi.html")


@login_required
def gym(request):
    return render(request ,"gym.html")
    
@login_required
def gym1(request):
    return render(request ,"gym1.html")

@login_required
def index1(request):
    return render(request ,"index1.html")