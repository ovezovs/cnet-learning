from django.contrib import admin
from .models import Course, Step

class StepInLine(admin.StackedInline):
    model = Step

class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInLine, ]

admin.site.register(Course, CourseAdmin)
admin.site.register(Step)

