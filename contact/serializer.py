from django.contrib.auth.models import User, Group
from rest_framework import serializers
from contact.models import Agent_Master,File_Data


class AgentMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent_Master
        fields = '__all__'

    def create(self, validated_data):
        """
        Create and return a new `notes` instance, given the validated data.
        """
        return Agent_Master.objects.create(**validated_data)

class AgentMasterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent_Master
        fields = ('pk','name','email','agent_id','phone','address')

    def create(self, validated_data):
        """
        Create and return a new `notes` instance, given the validated data.
        """
        return Agent_Master.objects.create(**validated_data)
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BulkExcelrecordcreateSerailizer(serializers.ListSerializer):
    def create(self, validated_data):
        ins_data=[File_Data(**item) for item in validated_data]
        print(ins_data)
        return File_Data.objects.bulk_create(ins_data)

class ExcelrecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=File_Data
        fields='__all__'
        list_serializer_class=BulkExcelrecordcreateSerailizer
    def create(self, validated_data):
        return File_Data.objects.create(**validated_data)

class ExcelrecordListSerializer(serializers.ModelSerializer):
    xl_data = serializers.JSONField()
    class Meta:
        model=File_Data
        fields=('name','phone','agent_id','xl_data','campaign','is_status')
        
    def create(self, validated_data):
        return File_Data.objects.create(**validated_data)