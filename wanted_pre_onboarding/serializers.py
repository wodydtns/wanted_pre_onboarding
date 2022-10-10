from rest_framework import serializers
from .models import Company, Applyment, Employment, User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class ApplymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applyment
        fields = '__all__'


class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
