from khunect.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'password', 'realname', 'nickname', 'email', 'phoneNum', 'image')