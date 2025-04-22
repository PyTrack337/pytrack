from django.contrib import admin
from .models import Course, Lesson, Exercise, LessonProgress

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Exercise)
admin.site.register(LessonProgress)