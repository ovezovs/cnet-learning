from django.test import TestCase
from .models import Course, Step
from django.utils import timezone
from datetime import timedelta


class CourseModelTests(TestCase):
    def test_course_creation(self):
        self.course = Course.objects.create(
            title='JavaScript Regular Expressions',
            description='Learn to write regular expressions in JS'
        )
        now = timezone.now() + timedelta(seconds=0.001)
        self.assertLess(self.course.created_at, now)

    def test_step_creation(self):
        step = Step.objects.create(
            title='Installing Text Editors',
            description='Install JavaScript text editor: Visual Studio Code',
            )
        self.assertIn(step, self.course.step_set.all())

