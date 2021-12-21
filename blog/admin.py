from django.contrib import admin
from .models import Topic, Blog, User

# Register your models here.

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Blog)
