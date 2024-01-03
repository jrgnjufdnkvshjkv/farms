from django.contrib import admin
from .models import About, Newsletter, Team, Features, Blog
# Register your models here.

admin.site.register(About),
admin.site.register(Team),
admin.site.register(Features),
admin.site.register(Blog),
admin.site.register(Newsletter)

