from django.db import models
from django.contrib import admin

class GitDatabase(models.Model):
    class Meta():
        permissions = (("view_profile", "can view staff details."),
                 ("view_repository", "can view income details"),
        )
    username_primary_key = models.CharField(max_length=30, help_text="User name must be unique", primary_key=True,unique=True)
    password = models.CharField(max_length=30)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    profile_photo = models.ImageField()
    email = models.EmailField(max_length=50,unique=True)

class GitAdmin(admin.ModelAdmin):
    list_display = ('username_primary_key', 'password', 'firstname', 'lastname','profile_photo','email')
