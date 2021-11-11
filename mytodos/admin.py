from django.contrib import admin

from mytodos.models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    '''Admin View for Todo'''

    list_display = ('title','description')
