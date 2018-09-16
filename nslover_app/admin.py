from django.contrib import admin
from django.db import models
from .models import Archives, Tags, Articles
from martor.widgets import AdminMartorWidget
# Register your models here.
admin.site.register(Archives)
admin.site.register(Tags)


class ArticlesModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Articles, ArticlesModelAdmin)