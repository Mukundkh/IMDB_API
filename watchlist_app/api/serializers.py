from django.forms import ValidationError
from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatForm

#Model Serializers
class MovieSerializers(serializers.ModelSerializer):
    #Customised Serializers fields
    len_name = serializers.SerializerMethodField()
    class Meta:
        model = WatchList
        #fields = '__all__'
        exclude = ['is_active']
        """
            If we want to exclude specific field we can write exclude keyword
            also.
        """
    
    def get_len_name(self, object):
        length = len(object.name)
        return length

    #field level validation
    def validate_name(self, value):
        if(len(value)<2):
            raise serializers.ValidationError("Name is too Short")
        else:
            return value;

    #Object level validation
    def validate(self, data):
        if(data['name'] == data['description']):
            raise serializers.ValidationError("both are same Error")
        else:
            return data 

#Serializers class

# class MovieSerializers(serializers.Serializer):

#     def name_len(self, value):
#         if len(value)<2:
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return value

#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_len])
#     description = serializers.CharField()
#     is_active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.is_active = validated_data.get('is_active', instance.is_active)
#         instance.save()
#         return instance

    

    #field level validation
    # def validate_name(self, value):
    #     if(len(value)<2):
    #         raise serializers.ValidationError("Name is Too Short")
    #     else:
    #         return value
