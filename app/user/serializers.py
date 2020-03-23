from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ serializer for the users object """
    class Meta:
        # model
        model = get_user_model()
        # fields to show in api
        fields = ('email', 'password', 'name')
        # configure extra settings
        # ensure the password is write only
        # the password is at least 5 char
        # add arguments for the fields
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5
            }
            }

    def create(self, validated_data):
        """ Create a new user with encrypted password and return it """
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """ serializer for the user authentications object """
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    # attrs every fields in serializers
    # will pass to attrs parameter
    def validate(self, attrs):
        """ validate and authenticate the user """
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        # add user to attrs to return it with all data
        attrs['user'] = user
        return attrs
