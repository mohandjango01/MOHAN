from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import serializers

from quiz.models import quizQuestionModel, quizChoiceModel

User = get_user_model


# <editor-fold desc="CHOICE CREATE">
class quizAdminChoiceCreateSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=500, required=True)

    def validate(self, data):
        if data["text"] == "":
            raise ValidationError("Choice text must be enter?")
        return data

    class Meta:
        model = quizChoiceModel
        fields = '__all__'


# </editor-fold>


# <editor-fold desc="GET ALL CHOICES">
class quizAdminGetAllChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = quizChoiceModel
        fields = ['text']


# </editor-fold>


# <editor-fold desc="GET ALL QUESTIONS">
class quizAdminGetAllQuestionSerializer(serializers.ModelSerializer):
    # choice = serializers.SerializerMethodField()
    #
    # def get_choice(self, obj):
    #     return obj.get_question_by_choices()

    quizChoiceModel_question = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='text'
    )

    class Meta:
        model = quizQuestionModel
        fields = ['title', 'created_by', 'start_date', 'end_date', 'quizChoiceModel_question']


# </editor-fold>


# # <editor-fold desc="QUESTION CREATE">
# class quizAdminQuestionCreateSerializer(serializers.ModelSerializer):
#     start_date = serializers.DateField(required=True)
#     end_date = serializers.DateField(required=True)
#
#     class Meta:
#         model = quizQuestionModel
#         fields = ['title', 'created_by', 'start_date', 'end_date']
#
#     def validate(self, data):
#         if data['start_date'] == "":
#             raise serializers.ValidationError('start date is must be fill')
#         if data['end_date'] == "":
#             raise serializers.ValidationError('end date is must be fill')
#         return data
#
#
# # </editor-fold>

# <editor-fold desc="QUESTION CREATE WITH CHOICES ALSO USING LISTFIELD ">
class quizAdminQuestionCreateSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(required=True)
    end_date = serializers.DateField(required=True)

    choices = serializers.ListField(
        child=serializers.CharField(max_length=1000000)
        , write_only=True
    )

    def validate(self, data):
        if data['start_date'] == "":
            raise serializers.ValidationError('start date is must be fill')
        if data['end_date'] == "":
            raise serializers.ValidationError('end date is must be fill')
        return data

    class Meta:
        model = quizQuestionModel
        fields = ['title', 'created_by', 'start_date', 'end_date', 'choices']

    def create(self, validated_data):
        choices = validated_data.pop('choices')
        question = quizQuestionModel.objects.create(**validated_data)
        for choice in choices:
            quizChoiceModel.objects.create(question=question, text=choice)
        return question

# </editor-fold>


# # <editor-fold desc="QUESTION CREATE WITH CHOICES ALSO USING LISTSERILAZERS">
# class quizAdminQuestionCreateSerializer(serializers.ModelSerializer):
#     start_date = serializers.DateField(required=True)
#     end_date = serializers.DateField(required=True)
#
#     choices = serializers.ListSerializer(
#         child=serializers.CharField(max_length=1000000)
#         , write_only=True
#     )
#
#     def validate(self, data):
#         if data['start_date'] == "":
#             raise serializers.ValidationError('start date is must be fill')
#         if data['end_date'] == "":
#             raise serializers.ValidationError('end date is must be fill')
#         return data
#
#     class Meta:
#         model = quizQuestionModel
#         fields = ['title', 'created_by', 'start_date', 'end_date', 'choices']
#
#     def create(self, validated_data):
#         choices = validated_data.pop('choices')
#         question = quizQuestionModel.objects.create(**validated_data)
#         for choice in choices:
#             quizChoiceModel.objects.create(question=question, text=choice)
#         return question
#
# # </editor-fold>


# <editor-fold desc="QUESTION CREATE WITH CHOICES ALSO USING LIST OF OBJECTS">

# class quizAdminQuestionCreateSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=500,required=True)
#     start_date = serializers.DateField(required=True)
#     end_date = serializers.DateField(required=True)
#
#     choices = serializers.ListSerializer(
#         child=serializers.CharField(max_length=1000000)
#         , write_only=True
#     )
#
#     def validate(self, data):
#         if data['start_date'] == "":
#             raise serializers.ValidationError('start date is must be fill')
#         if data['end_date'] == "":
#             raise serializers.ValidationError('end date is must be fill')
#         return data
#
#     class Meta:
#         model = quizQuestionModel
#         fields = ['title', 'created_by', 'start_date', 'end_date', 'choices']
#
#     def create(self, validated_data):
#         choices = validated_data.pop('choices')
#         question = quizQuestionModel.objects.create(**validated_data)
#         for choice in choices:
#             quizChoiceModel.objects.create(question=question, text=choice)
#         return question
#
#
#     def update(self, instance, validated_data):
#         instance.email = validated_data.get('email', instance.email)
#         instance.content = validated_data.get('content', instance.content)
#         instance.created = validated_data.get('created', instance.created)
#         return instance

# </editor-fold>
