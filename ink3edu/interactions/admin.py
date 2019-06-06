from django.contrib import admin
from .models import Student, Mentor, Role, Group

admin.site.register(Student)
admin.site.register(Mentor)
admin.site.register(Role)
admin.site.register(Group)