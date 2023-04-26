from django.contrib import admin
from .models import Todo, student


admin.site.register(Todo)
# Register your models here.


class studentadmin(admin.ModelAdmin):

    list_display = ("id", "cName", "cSex", "cBirthday", "cEmail", "cPhone", "cAddr")
    list_filter = ("cName", "cSex")
    search_fields = ("cName",)
    ordering = ("id",)

admin.site.register(student, studentadmin)