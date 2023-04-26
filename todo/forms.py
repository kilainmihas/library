from django.forms import ModelForm #繼承modelForm 方便取用以設定的欄位名稱
from .models import Todo

class Todoform(ModelForm):
    class Meta:
        model = Todo 
        fields = ['title','text','date_completed','important']