from rest_framework import serializers, status

from accounts.api_v1_client.serializers import accountsClientUserdetailsSerializer
from student.models import studentStudentModel


# <editor-fold desc="GET ALL STUDENTS">
class studentAdminGetAllStudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentStudentModel
        fields = ['slug', 'student', 'age', 'city', ]


# </editor-fold>


# # <editor-fold desc="STUDENTS CREATE ">
# class studentAdminStudentCreateSerializer(serializers.ModelSerializer):
#     def validate(self, data):
#         student = data.get('student', None)
#         print("student=====", student)
#         try:
#             if studentStudentModel.objects.filter(student=student).exists():
#                 raise serializers.ValidationError({'msg':"Student already exist","status":status.HTTP_400_BAD_REQUEST})
#         except:
#             pass
#
#         return data
#
#     class Meta:
#         model=studentStudentModel
#         fields = ['id', 'student', 'age', 'city', ]
#
#
# # </editor-fold>

# <editor-fold desc="STUDENTS CREATE AND DELETE ">
class studentAdminStudentCreateSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    city = serializers.CharField()

    # student = serializers.SerializerMethodField()
    #
    def validate_student(self, data):
        print("student=====", data)
        return data

    class Meta:
        fields = ['slug', 'student', 'age', 'city', ]

    def create(self, validated_data):
        student_user = self.context['request'].user

        student_instance = studentStudentModel.objects.filter(student=student_user).exists()
        if not student_instance:
            student = studentStudentModel.objects.create(
                student=student_user, **validated_data
            )
            print("created")
        else:
            student = studentStudentModel.objects.get(student=student_user)
            student.delete()
            print("deleted")

        return validated_data


# </editor-fold>


# <editor-fold desc="GET ALL STUDENTS ">

def age_check(value):
    if value <= 18:
        raise serializers.ValidationError(
            {"msg": "Your Not eligible for election", "status": status.HTTP_400_BAD_REQUEST})


class studentAdminUpdateStudentsSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(validators=[age_check])

    class Meta:
        model = studentStudentModel
        fields = ['age']


# </editor-fold>


# <editor-fold desc="STUDENTS CREATE AND DELETE and GET ALL STUDENTS AND UPDATE THE STUDENT">
class studentAdminStudentCreateAndGetAllStudentsSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    city = serializers.CharField()

    # student = serializers.SerializerMethodField()
    #
    def validate_student(self, data):
        print("student=====", data)
        return data

    class Meta:
        fields = ['slug', 'student', 'age', 'city', ]

    def create(self, validated_data):
        student_user = self.context['request'].user

        student_instance = studentStudentModel.objects.filter(student=student_user).exists()
        if not student_instance:
            student = studentStudentModel.objects.create(
                student=student_user, **validated_data
            )
            print("created")
        else:
            student = studentStudentModel.objects.get(student=student_user)
            student.delete()
            print("deleted")

        return validated_data

    def update(self, instance, validated_data):
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        return instance

# </editor-fold>
