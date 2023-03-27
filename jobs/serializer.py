from .models import *
from rest_framework import serializers


# user serializer
class UserSerializer(serializers.ModelSerializer):
    """
    user serializer
    """
    class Meta:
        model = User
        exclude = ('password', 'user_permissions', 'groups',
                   'is_superuser', 'is_active', 'date_joined', 'last_login')


# create user serializer
class UserCreationSerializer(serializers.ModelSerializer):
    """
        This method is used to serialize the user object
        Args:
            user: user object
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# jobs category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# jobs serializer
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'company_name', 'company_website', 'title', 'slug', 'category',
                  'salary_range', 'job_type', 'job_description', 'location', 'application_deadline', 'experience', 'qualification', 'link_to_job', 'user', 'created_at')
        extra_kwargs = {'user': {'read_only': True}}


# create job serializer
class CreateJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('company_name', 'company_website', 'title', 'category',
                  'salary_range', 'job_type', 'job_description', 'location', 'application_deadline', 'experience', 'qualification', 'link_to_job', 'user')

    # create job
    def create(self, validated_data):
        job = Job.objects.create(**validated_data)
        return job
