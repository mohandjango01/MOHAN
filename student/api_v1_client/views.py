from rest_framework import viewsets
from student.models import studentStudentModel
from .serializers import studentClientStudentSerializer


# <editor-fold desc="STUDENT CREATE,UPDATE,DELETE,">
class studentClientStudentCurd(viewsets.ModelViewSet):
    queryset = studentStudentModel.objects.all()
    serializer_class = studentClientStudentSerializer

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

    def perform_update(self, serializer):
        serializer.save(student=self.request.user)

# </editor-fold>
