from rest_framework import serializers
from .models import User,Organisation,Permission

class UserSerializers(serializers.ModelSerializer): 
    class Meta:
        model=User
        fields=['name','email']


class OrganisationSerializers(serializers.ModelSerializer): 
    class Meta:
        model=Organisation
        fields=['name']


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('user_email', 'organisation_name', 'access_level')


class DeletePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('user_email', 'organisation_name')
