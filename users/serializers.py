from rest_framework import serializers

# Model
from django.contrib.auth import get_user_model, password_validation, hashers
User = get_user_model()

# Serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        # Remove plain text password and the password_confirmation from the dictionary of fields (data)
        password = data.pop('password') # Removes plain text password, later we'll add password back as a hash
        password_confirmation = data.pop('password_confirmation') # We won't re-add this field as it's not on the model

        # check the plain text password against the password_confirmation, raise ValidationError if they don't match
        if password != password_confirmation:
            raise serializers.ValidationError({ 'password_confirmation': 'Passwords do not match.' })

        # If passwords matched, run validators against the password (common password, length etc.)
        password_validation.validate_password(password)

        # Hash the plain text password and add it back to the data dictionary
        data['password'] = hashers.make_password(password)

        # Return the data, whether it's modified or unmodified
        return data
    
        
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password_confirmation', 'admin', )
