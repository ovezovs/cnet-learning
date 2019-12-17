
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.course_list, name='list'),
    path('<int:course_pk>/<int:step_pk>/', views.step_detail, name='step'),
    path('<int:pk>/', views.course_detail, name='detail'),
]

