from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import SlugField
from rest_framework.validators import UniqueValidator, UniqueForDateValidator

from accounts.api_v1_client.serializers import accountsClientUserdetailsSerializer
from quiz.models import quizQuestionModel, quizChoiceModel

User = get_user_model


# <editor-fold desc="CHOICES MODEL">
class quizClientChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = quizChoiceModel
        fields = "__all__"


# </editor-fold>

# <editor-fold desc="GET ALL QUESTION MODEL">
class quizClientQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = quizQuestionModel
        fields = ['title', 'status', 'created_by', 'start_date', 'end_date', 'choices']


# </editor-fold>


# <editor-fold desc="VALIDATOR USING FOR QUESTION TEXT MUST BE TEXT ">
def function(value):
    for data in value:
        data.isdigit()
        raise serializers.ValidationError("question can't be numeric")


# </editor-fold>


# <editor-fold desc="QUESTION MODEL CREATE">
class quizClientQuestionCreateSerializer(serializers.ModelSerializer):
    choices = serializers.ListField(child=serializers.CharField(max_length=200), write_only=True)
    title = serializers.CharField(max_length=100, validators=[function])  # validator using
    created_by = accountsClientUserdetailsSerializer(read_only=True)

    # unique Validator
    slug = SlugField(
        max_length=100,
        validators=[UniqueValidator(queryset=quizQuestionModel.objects.all())], read_only=True
    )

    def validate_created_by(self, value):
        print(value, '-----------value======')
        return value

    class Meta:
        model = quizQuestionModel
        fields = ['title', 'slug', 'status', 'created_by', 'start_date', 'end_date', 'choices']

        # extra_kwargs = {'client': {'required': False}}

        # validators = [
        #     UniqueForDateValidator(
        #         queryset=quizQuestionModel.objects.all(),
        #         field='slug',
        #         date_field='date_created'
        #     )
        # ]

    def create(self, validated_data):
        choices = validated_data.pop('choices', None)
        title = validated_data.get('title', None)
        created_by = validated_data.get('created_by', None)
        print("choicess---------------", choices, 'title==', title)
        question_instance = quizQuestionModel.objects.filter(title__iexact=title, created_by=created_by)
        print("Questions===============", question_instance)

        print(type(question_instance))

        if not question_instance.exists():
            question_new = quizQuestionModel.objects.create(**validated_data)
            print("Questions===============", question_new)
            for choice in choices:
                choice = quizChoiceModel.objects.create(question=question_new, text=choice)
                print("if question is there then choice is create")
        else:
            if question_instance.exists():
                print("remove")
                question_instance.delete()

        return validated_data
# </editor-fold>
