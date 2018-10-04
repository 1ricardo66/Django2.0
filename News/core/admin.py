from django.contrib import admin
from .models import New,Author

admin.site.register(Author)
class NewAdmin(admin.ModelAdmin):
    list_display = ("title","date","author","status",)
    search_fields = ("title","date","author","tags","status",)

admin.site.register(New,NewAdmin)
# Register your models here.
