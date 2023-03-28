"""
URLs for django_course.
"""
from django.urls import re_path, path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

from .views import GetCourses

urlpatterns = [
    path('courses/', GetCourses.as_view(), name='course-list'),
]

# urlpatterns = [
#     # TODO: Fill in URL patterns and views here.
#     # re_path(r'', TemplateView.as_view(template_name="django_course/base.html")),
# ]
