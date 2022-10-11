from rest_framework import serializers

from student.models import studentStudentModel


# <editor-fold desc="STUDENT ">
class studentClientStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentStudentModel
        fields = '__all__'
        read_only_fields=('student',)
# </editor-fold>
