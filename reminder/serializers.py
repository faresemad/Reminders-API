from rest_framework import serializers
from .models import Reminder, Category

class ReminderSerializer(serializers.ModelSerializer):
    auther = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = Reminder
        fields = '__all__'
        
    def get_auther(self, obj):
        return f"{obj.auther.first_name} {obj.auther.last_name}"
    
    def get_category(self, obj):
        try:
            return str(obj.category.name)
        except AttributeError:
            return f"Notes"

    def create(self, validated_data):
        validated_data['auther'] = self.context['request'].user
        return super().create(validated_data)


class CategorySerializer(serializers.ModelSerializer):
    auther = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = '__all__'
        
    def get_auther(self, obj):
        return f"{obj.auther.first_name} {obj.auther.last_name}"
    
    def create(self, validated_data):
        validated_data['auther'] = self.context['request'].user
        return super().create(validated_data)
