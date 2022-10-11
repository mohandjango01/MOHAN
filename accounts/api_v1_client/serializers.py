from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


# <editor-fold desc="USER CREATE ">
class accountsClientUserCreateSerializer(serializers.ModelSerializer):
    dob = serializers.DateField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('phone', 'password', 'email', 'dob', 'slug')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user
# </editor-fold>


# <editor-fold desc="GET USER DETAIL">
class accountsClientUserdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',)


# </editor-fold>