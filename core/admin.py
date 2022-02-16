from django.contrib import admin
from core.models import Contact_us,Category,Foodcard

# Register your models here.

class Contact_usAdmin(admin.ModelAdmin):
    list_display = ("email", "sent_at")

admin.site.register(Contact_us, Contact_usAdmin)
admin.site.register(Category)
admin.site.register(Foodcard)
