from django.contrib import admin

from .models import *

#registrar edición clase BD
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Vote)