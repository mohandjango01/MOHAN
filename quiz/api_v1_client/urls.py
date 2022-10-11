from django.urls import path

from quiz.api_v1_client.views import quizClientQuestionCreateGenericsView, quizClientQuestionDetailsAPIView

urlpatterns = [

    # <editor-fold desc="">
    path('question-create/', quizClientQuestionCreateGenericsView.as_view(),
         name='quizClientQuestionCreateGenericsViewURL'),
    # </editor-fold>

    # <editor-fold desc="">
    path('question-details/<slug>/', quizClientQuestionDetailsAPIView.as_view(),
         name='quizClientQuestionDetailsAPIViewURL'),
    # </editor-fold>





]
