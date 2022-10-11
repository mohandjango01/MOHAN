from django.urls import path

from quiz.api_v1_admin.views import quizAdminQuestionCreateGenericsView, quizAdminQuestionDetailsAPIView, \
    quizAdminChoiceCreateGenericsView, quizAdminChoiceDetailsAPIView

urlpatterns = [
    # <editor-fold desc="QUESTION CREATE">
    path('question-create/', quizAdminQuestionCreateGenericsView.as_view(),
         name='quizAdminQuestionCreateGenericsViewURL'),
    # </editor-fold>

    # <editor-fold desc="QUESTION DETAILS BY USING QUESTION SLUG">
    path('question-details/<slug>/', quizAdminQuestionDetailsAPIView.as_view(),
         name='quizAdminQuestionDetailsAPIViewURL'),
    # </editor-fold>

    # <editor-fold desc="CHOICE CREATE">
    path('choice-create/', quizAdminChoiceCreateGenericsView.as_view(),
         name='quizAdminChoiceCreateGenericsViewURL'),
    # </editor-fold>

    # <editor-fold desc="CHOICE DETAILS BY USING CHOICE SLUG">
    path('choice-details/<slug>/', quizAdminChoiceDetailsAPIView.as_view(),
         name='quizAdminChoiceDetailsAPIViewURL'),
    # </editor-fold>
]
