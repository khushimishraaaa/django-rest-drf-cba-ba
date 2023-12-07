from rest_framework import serializers
from .models import *

class TeacherSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields =  ('f_name', 'l_name', 'subject')

