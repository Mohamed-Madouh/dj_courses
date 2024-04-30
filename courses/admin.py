from django.contrib import admin # type: ignore
from .models import Section ,courses,course_content
# Register your models here.
admin.site.register(Section)
admin.site.register(courses)
admin.site.register(course_content)