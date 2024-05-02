from django.contrib.admin import register, ModelAdmin
from .models import User, Command

@register(User)
class UserAdmin(ModelAdmin):
    pass

@register(Command)
class CommandAdmin(ModelAdmin):
    pass
