from django.contrib import admin
from .models import Training, Section, Chapter, Status, Category

admin.site.register(Training)
admin.site.register(Section)
admin.site.register(Chapter)
admin.site.register(Status)
admin.site.register(Category)