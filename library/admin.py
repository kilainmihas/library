from django.contrib import admin
from .models import*

# Register your models here.


class BookInline(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display =  ('last_name','first_name', 'date_of_birth', 'date_of_death')
    # fields 變更文字編排 ()內的物件會水平顯示 單一物件則垂直顯示
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]



class BooksinstanceInline(admin.TabularInline):
    model = Bookinstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksinstanceInline]



@admin.register(Bookinstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book','borrower' , 'status','due_back')
    #list_filter 可使用物件篩選
    list_filter = ('status', 'due_back')
    # fieldsets 可把物件分為幾個區塊顯示
    fieldsets = (
        #()內是一個區塊  EX(區塊名,{'fields':(物件名稱)})
        (None,{
            'fields':('book', 'imprint', 'id')
        }),


        ('Availability',{
            'fields': ('status', 'due_back','borrower')
        })
    )



admin.site.register(Genre)


