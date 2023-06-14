from django.contrib import admin
from .models import Artist, Tag, Group
# Register your models here.

admin.site.register(Artist)
admin.site.register(Tag)
admin.site.register(Group)
