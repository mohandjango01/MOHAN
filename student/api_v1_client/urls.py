
from rest_framework.routers import DefaultRouter
from .views import studentClientStudentCurd
from django.urls import path, include

router = DefaultRouter()
# <editor-fold desc="STUDENT GET ALL,CREATE,UPDATE,DELETE">
router.register('student_list', studentClientStudentCurd)
# </editor-fold>

urlpatterns = [
    path('', include(router.urls)),
]