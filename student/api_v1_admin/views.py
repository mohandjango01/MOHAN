from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView

from student.api_v1_admin.serializers import studentAdminStudentCreateSerializer, studentAdminGetAllStudentsSerializer, \
    studentAdminUpdateStudentsSerializer, studentAdminStudentCreateAndGetAllStudentsSerializer
from student.models import studentStudentModel


# <editor-fold desc="GET ALL STUDENTS">
class studentAdminStudentListApiView(ListAPIView):
    queryset = studentStudentModel.objects.all()
    serializer_class = studentAdminGetAllStudentsSerializer


# </editor-fold>


# <editor-fold desc="NEW STUDENT CREATE AND DELETED IF EXIST">
class studentAdminStudentCreateApiView(CreateAPIView):
    queryset = studentStudentModel.objects.all()
    serializer_class = studentAdminStudentCreateSerializer


# </editor-fold>


# <editor-fold desc="STUDENT UPDATE BY USING STUDENT SLUG">
class studentAdminStudentUpdateApiView(UpdateAPIView):
    queryset = studentStudentModel.objects.all()
    serializer_class = studentAdminUpdateStudentsSerializer
    lookup_field = 'slug'


# </editor-fold>


# <editor-fold desc="STUDENT DELETE BY USING SLUG">
class studentAdminStudentDeleteApiView(DestroyAPIView):
    queryset = studentStudentModel.objects.all()
    serializer_class = studentAdminUpdateStudentsSerializer
    lookup_field = 'slug'


# </editor-fold>


# <editor-fold desc="GET ALL STUDENT AND CREATE STUDENT">
class studentAdminStudentListAndCreateAPIview(ListCreateAPIView):
    queryset = studentStudentModel.objects.all()
    serializer_class = studentAdminStudentCreateAndGetAllStudentsSerializer
# </editor-fold>


# <editor-fold desc="GET STUDENT AND REMOVE STUDENT">
class studentAdminStudentGetAndRemoveAPIview(RetrieveDestroyAPIView):
    queryset = studentStudentModel.objects.all()
    serializer_class = studentAdminGetAllStudentsSerializer
    lookup_field = 'slug'
# </editor-fold>

# <editor-fold desc="GET STUDENT AND UPDATE STUDENT">
class studentAdminStudentGetAndUpdateAPIview(RetrieveUpdateAPIView):
    queryset = studentStudentModel.objects.all()
    serializer_class = studentAdminStudentCreateAndGetAllStudentsSerializer
    lookup_field = 'slug'
# </editor-fold>

# <editor-fold desc="GET STUDENT AND UPDATE STUDENT">
class studentAdminStudentGetAndUpdateAndDeleteAPIview(RetrieveUpdateDestroyAPIView):
    queryset = studentStudentModel.objects.all()
    serializer_class = studentAdminStudentCreateAndGetAllStudentsSerializer
    lookup_field = 'slug'
# </editor-fold>