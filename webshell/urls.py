from django.urls import re_path
from .views import execute_script_view

urlpatterns = [
    re_path(r'^execute/$', execute_script_view, name='execute-script'),
]
