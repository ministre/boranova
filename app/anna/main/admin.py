from django.contrib import admin
from .models import Counter, File, Photo, Video

admin.site.register(Counter)
admin.site.register(File)
admin.site.register(Photo)
admin.site.register(Video)
