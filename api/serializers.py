from rest_framework import serializers
from .models import *



# Validators

def start_with_e(value):
    if value[0].lower() != 'e':
        raise serializers.ValidationError('Name should be start with E')
    return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_e])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # field level validation
    def validate_roll(self,value):
        if value > 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # field level validation
    def validate(self,data):

        nm = data.get('name')
        ct = data.get('city')

        if nm.lower() == 'emon' and ct.lower() != 'dhaka':
            raise serializers.ValidationError('City must be dhaka as you are emon')
        return data


# Model Serializer
class StudentMSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['id','name', 'roll', 'city']
        # fields = '__all__'
        # exclude = ['roll']
        # read_only_fields = ['name', 'roll']
        # extra_kwargs = {'name': {'read_only':True}}
    def validate_roll(self,value):
        if value > 200:
            raise serializers.ValidationError('Seat Full')
        return value


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only = True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only = True, view_name = 'song-detail')
    song = serializers.SlugRelatedField(many=True, read_only = True, slug_field = 'title')
    # song = serializers.SlugRelatedField(many=True, read_only = True, slug_field = 'duration')
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']

class StudentHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'roll', 'city', 'passby']
