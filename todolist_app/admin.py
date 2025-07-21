from django.contrib import admin
from .models import tasklistmodel
from .models import contactmodel


# Register your models here.
admin.site.register(tasklistmodel)

admin.site.register(contactmodel)

