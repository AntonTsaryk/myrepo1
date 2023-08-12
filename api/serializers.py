from rest_framework import serializers
from .models import User, ServiceCategory, Worker, Job, JobOffer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
    # specializations = serializers.StringRelatedField(many=True)
    class Meta:
        model = Worker
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    # to see string client name instead of id
    # client = serializers.StringRelatedField()
    class Meta:
        model = Job
        fields = '__all__'


class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = '__all__'
