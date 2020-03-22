from django.contrib.auth import get_user_model

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
