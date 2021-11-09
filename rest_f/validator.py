from rest_framework.utils.representation import smart_repr
from rest_framework import serializers
import re


class AddressValidator:
    message = "Validation error: "

    def __init__(self, message=None):
        self.validated_field = ''
        self.validated_data = None
        self.message = message or self.message

    def __call__(self, attrs):
        message = self.message
        if 'apartamenst' in attrs and attrs['apartamenst'] <= 0:
            message = 'cannot be less than zero'
            self.raize_error(attrs, 'apartamenst', message)
        if 'city' in attrs and len(attrs['city']) < 3:
            message = 'cannot be less than three'
            self.raize_error(attrs, 'city', message)
        if 'country' in attrs and len(attrs['country']) < 3:
            message = 'cannot be less than three'
            self.raize_error(attrs, 'country', message)
        if 'house_num' in attrs and attrs['house_num'] <= 0:
            message = 'cannot be less than zero'
            self.raize_error(attrs, 'house_num', message)
        if 'street' in attrs and not 'street' in attrs['street']:
            message = 'there must be an inscription street'
            self.raize_error(attrs, 'street', message)
        if 'zip_code' in attrs and not len(str(attrs['zip_code'])) == 5:
            message = 'cannot be five digits'
            self.raize_error(attrs, 'zip_code', message)

    def raize_error(self, attrs, field_name, message):
        message = self.message + f'The {field_name} field {message}.'
        self.validated_field = field_name
        self.validated_data = attrs[field_name]
        raise serializers.ValidationError(message, code=field_name)

    def __repr__(self):
        return f'<{self.__class__.__name__}({self.validated_field}={self.validated_data})>'
