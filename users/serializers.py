from rest_framework import serializers, validators
from users.models import MyUser


# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(source='username', validators=[
#         validators.UniqueValidator(MyUser.objects.all())
#     ])
#     password = serializers.CharField(min_length=8, max_length=16, write_only=True)
#
#     def create(self, validated_data):
#         user = MyUser.objects.create(
#             username=validated_data['username'],
#         )
#
#         user.set_password(validated_data['password'])
#         user.save(update_fields=['password'])

class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
        extra_kwargs = {"id": {"read_only":True}}
