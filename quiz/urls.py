from django.urls import path, include

urlpatterns = [
    # <editor-fold desc="ALBUM AND MUSICIAN CREATE AND DETAILS ">
    path('api/admin/v1/', include('quiz.api_v1_admin.urls')),

    # </editor-fold>

    path('api/client/v1/', include('quiz.api_v1_client.urls')),
]