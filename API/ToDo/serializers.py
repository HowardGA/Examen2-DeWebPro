from rest_framework import serializers
from ToDo.models import Task, Area, Comment, CustomUser



# Detail Task Serializer
class DetailTaskSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'state', 'created_at', 'user', 'area']
        
    def get_user(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    def get_area(self, obj):
        return obj.area.area_name
    
# TASk Serializer
class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# Area Serializer
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

        
# User Serilializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'phone_number', 'user_area', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            user_area=validated_data['user_area'],
            password=validated_data['password']
        )
        return user

# Serializers that were explicitly asked within the instructions:
# Task IDs Serializer
class TaskIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id']

# Task IDs and Titles Serializer
class TaskIDTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title']

# Unresolved Tasks (IDs and Titles) Serializer
class UnresolvedTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title']
        extra_kwargs = {
            'id': {'read_only': True}
        }
    
    def get_queryset(self):
        return Task.objects.filter(state='PENDING')

# Resolved Tasks (IDs and Titles) Serializer
class ResolvedTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title']
        extra_kwargs = {
            'id': {'read_only': True}
        }
    
    def get_queryset(self):
        return Task.objects.filter(state='DONE')

# Task IDs and UserIDs Serializer
class TaskUserIDSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    
    class Meta:
        model = Task
        fields = ['id', 'user_id']

# Resolved Tasks (IDs and UserIDs) Serializer
class ResolvedTasksUserIDSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    
    class Meta:
        model = Task
        fields = ['id', 'user_id']
    
    def get_queryset(self):
        return Task.objects.filter(state='DONE')

# Unresolved Tasks (IDs and UserIDs) Serializer
class UnresolvedTasksUserIDSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id')
    
    class Meta:
        model = Task
        fields = ['id', 'user_id']
    
    def get_queryset(self):
        return Task.objects.filter(state='PENDING')
