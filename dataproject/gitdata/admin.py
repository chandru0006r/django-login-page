from django.contrib import admin
from .models import GitDatabase,GitAdmin


admin.site.register(GitDatabase,GitAdmin)
