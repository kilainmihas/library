from datetime import datetime
from django.shortcuts import render

# Create your views here.
def ntime(request):
    nowtime = datetime.now().strftime("%Y-%m-%d %H: %M: %S")
    return render(request,'login.html',{'time':nowtime})

def register(request):
    