from django.contrib import admin
from .models import Cat


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'breed', 'age', 'is_cute', 'created_at')
    list_filter = ('is_cute', 'breed')
    search_fields = ('name', 'breed')
