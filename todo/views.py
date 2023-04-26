from ast import Try
from datetime import datetime
from email import message
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout , authenticate
from .models import Todo, student
from .forms import Todoform
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import student
import random

# Create your views here.


#任何網頁預設都是以GET為主 ，所以要使用if 來檢查是否使用POST

def ntime(request):
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return render(request,'base.html','login.html',{'time':nowtime})


#註冊
def register(request):
    message=''
    if request.method=="POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(password1)>=8 and password1==password2:
            
            if User.objects.filter(username=username).exists(): #檢查資料庫是否存在相同使用者
                message='帳號重複'
            else:
                user = User.objects.create_user(username=username,password=password1)
                user.save()

                message='帳號建立成功!'
                
                login(request, user) #django內建登入方法

                return redirect('login')   #redirect() 重新導向另一個網頁
        else:
            if len(password1)<8:
                message='密碼過短'
            else:
                message='兩次密碼不同!'  


    return render(request,'register.html',{'form': UserCreationForm(),
                                            'message': message })

#清單
@login_required
def todolist(request):
    # todos = Todo.objects.all() 取得全部資料
    todos = Todo.objects.filter(user=request.user) #取得使用者資料

    for todo in todos:
        print(f'{todo.id}-{todo.title}')

    return render(request, 'todolist.html',{'todos': todos})

#建立viewtodo pk(primary key)
@login_required
def viewtodo(request, todo_id):
    message=''
    todo = get_object_or_404(Todo, pk=todo_id)
    form=Todoform(instance=todo)
    if request.method =="POST":
        try:
            form = Todoform(request.POST,instance=todo)
            form.save()
            return redirect('todolist')
        except Exception as e:
            print(e)
            message='資料輸入錯誤，請重新輸入.'

    
    return render(request,'viewtodo.html', {'todo':todo, 'form': form, 'message':message})

#建立清單
@login_required
def createtodo(request):
    message = ''
    if request.method =="POST":
        try:
         form = Todoform(request.POST)
         todo = form.save(commit=False)
         todo.user = request.user
         todo.save()

         return redirect('todolist')
        except Exception as e:
            print(e)
            message='資料輸入錯誤，請重新輸入.'
   
    return render(request, 'createtodo.html',{'form':Todoform(), 'message':message})
#刪除清單
@login_required
def deletetodo(request, todo_id):
    if request.method =="POST":
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.delete()

        return redirect('todolist')
#完成清單
@login_required
def completetodo(request, todo_id):
    if request.method =="POST":
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.date_completed=datetime.now()
        todo.save()

        return redirect('todolist')

@login_required
def completed(request):
    todos = Todo.objects.filter(user=request.user)

    return render(request, 'completed.html', {"todos":todos})


def user_login(request):
    message = ''
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        #註冊功能
        if request.POST.get("register"):
            return redirect("register")
        #登入功能
        if request.POST.get("login"):
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)  #authenticate 驗證是否有該帳號密碼 
             #有則登入
            if user:
                login(request, user)
                return redirect('login')

            message='登入失敗'


    return render(request,'login.html', {'message': message,'time':nowtime})
#登出
@login_required
def user_logout(request):
    logout(request)

    return redirect('login')



@login_required
def card(request):
    message=''
    nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cards = {'N':0.75, 'R':0.22, 'SSR':0.29, 'UR':0.01}
    if request.GET.get():


        return render(request,'card.html', {'message': message,'time':nowtime})



def listall(request):
    students = student.objects.all().order_by("id")
    return render(request, "listall.html", locals())


def insert(request): #新增資料
    if request.method == "POST":
        cName = request.POST["name"]
        cSex = request.POST["sex"]
        cBirthday = request.POST["birthday"]
        cEmail = request.POST["Email"]
        cPhone = request.POST["phone"]
        cAddr = request.POST["addr"]
        unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr)
        unit.save()
        students = student.objects.all().order_by('id')
        return render(request, "listall.html", locals())
    else:
        return render(request, "insert.html", locals())

def modify(request):#修改資料
    name = request.GET['name']
    unit = student.objects.get(cName=name)
    if request.method == "POST":
        unit.cName = request.POST['name']
        unit.cSex = request.POST['sex']
        unit.cBirthday = request.POST['brithday']
        unit.cEmail = request.POST["Email"]
        unit.cPhone = request.POST["phone"]
        unit.cAddr = request.POST["addr"]
        unit.save()
        students = student.objects.all().order_by('id')
        return render(request, "listall.html", locals())
    
    else:
        sex = unit.cSex
        birthday = unit.cBirthday
        email = unit.cEmail
        phone = unit.cPhone
        addr = unit.cAddr
        return render(request, "modify.html", locals())

def delete(request, id = None): #刪除資料
    name = request.GET["name"]
    unit = student.objects.get(cName = name)
    unit.delete()
    student.objects.all().order_by("id")
    return render(request, "listall.html", locals())


