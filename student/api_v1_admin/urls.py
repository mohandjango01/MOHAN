from django.urls import path
from .views import studentAdminStudentListApiView, studentAdminStudentCreateApiView, studentAdminStudentUpdateApiView, \
    studentAdminStudentDeleteApiView, studentAdminStudentListAndCreateAPIview, studentAdminStudentGetAndRemoveAPIview, \
    studentAdminStudentGetAndUpdateAPIview, studentAdminStudentGetAndUpdateAndDeleteAPIview

urlpatterns = [
    # <editor-fold desc="GET ALL STUDENTS">
    path('student/', studentAdminStudentListApiView.as_view(), name="studentAdminStudentListApiViewURL"),
    # </editor-fold>

    # <editor-fold desc="STUDENT CREATE">
    path('student-create/', studentAdminStudentCreateApiView.as_view(), name="studentAdminStudentCreateApiViewURL"),
    # </editor-fold>

    # <editor-fold desc="STUDENT UPDATE BY USING SLUG">
    path('student-update/<slug>/', studentAdminStudentUpdateApiView.as_view(),
         name="studentAdminStudentUpdateApiViewURL"),
    # </editor-fold>

    # <editor-fold desc="STUDENT DELETE">
    path('student-remove/<slug>/', studentAdminStudentDeleteApiView.as_view(),
         name="studentAdminStudentDeleteApiViewURL"),
    # </editor-fold>

    # <editor-fold desc="STUDENT CREATE AND GET ALL STUDENTS">
    path("students/", studentAdminStudentListAndCreateAPIview.as_view(),
         name="studentAdminStudentListAndCreateAPIviewURL"),
    # </editor-fold>

    # <editor-fold desc="GET THE STUDENT AND REMOVE BY SUING STUDENT SLUG">
    path('delete-student/<slug>/', studentAdminStudentGetAndRemoveAPIview.as_view(),
         name="studentAdminStudentGetAndRemoveAPIviewURL"),
    # </editor-fold>

    # <editor-fold desc="GET THE STUDENT BY USING STUDENT SLUG AND UPDATE THE VALUES">
    path('update-student/<slug>/', studentAdminStudentGetAndUpdateAPIview.as_view(),
         name="studentAdminStudentGetAndUpdateAPIviewURL"),
    # </editor-fold>

    # <editor-fold desc="STUDENT GET BY USING STUDENT SLUG AND UPDATE AND DELETE">
    path('retrive-update-destroy-student/<slug>/', studentAdminStudentGetAndUpdateAndDeleteAPIview.as_view(),
         name="studentAdminStudentGetAndUpdateAndDeleteAPIviewURL")
    # </editor-fold>

]
