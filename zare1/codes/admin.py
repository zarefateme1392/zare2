from django.contrib import admin

# Register your models here.
from .models import Code

#admin.site.register(Code)
@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    list_display=('number','user')
