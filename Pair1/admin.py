from django.contrib import admin
from .models import Review
from .models import User
# Register your models here.

admin.site.register(Review)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =(
        'user_id',
        'user_pw',
        'user_name',
        'user_email',
        'user_register_dttm'
    )