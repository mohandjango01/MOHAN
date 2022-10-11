from rest_framework import generics, status, filters
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.api_v1_admin.serializers import quizAdminQuestionCreateSerializer, \
    quizAdminGetAllQuestionSerializer, quizAdminChoiceCreateSerializer, \
    quizAdminGetAllChoiceSerializer
from quiz.models import quizQuestionModel, quizChoiceModel


# <editor-fold desc="GET ALL QUESTION AND CREATE QUESTION">
class quizAdminQuestionCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = quizAdminGetAllQuestionSerializer
    queryset = quizQuestionModel.objects.all()
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = LimitOffsetPagination
    search_fields = ["title","start_date","end_date",]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = quizAdminQuestionCreateSerializer(data=request.data,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>

# <editor-fold desc="QUESTION DETAILS">
class quizAdminQuestionDetailsAPIView(APIView):
    serializer_class = quizAdminGetAllQuestionSerializer
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = quizQuestionModel.objects.get(slug=slug)
        serializer = quizAdminGetAllQuestionSerializer(data,context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = quizQuestionModel.objects.get(slug=slug)
        serializer = quizAdminGetAllQuestionSerializer(data=request.data, instance=data, partial=True,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = quizQuestionModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
# </editor-fold>

# <editor-fold desc="GET ALL CHOICE AND CREATE CHOICE">
class quizAdminChoiceCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = quizAdminGetAllChoiceSerializer
    queryset = quizChoiceModel.objects.all()
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = LimitOffsetPagination
    search_fields = ["title","start_date","end_date",]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = quizAdminChoiceCreateSerializer(data=request.data,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>

# <editor-fold desc="CHOICE DETAILS">
class quizAdminChoiceDetailsAPIView(APIView):
    serializer_class = quizAdminGetAllChoiceSerializer
    permission_classes = (IsAuthenticated,)
    authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = quizChoiceModel.objects.get(slug=slug)
        serializer = quizAdminGetAllChoiceSerializer(data,context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = quizChoiceModel.objects.get(slug=slug)
        serializer = quizAdminGetAllChoiceSerializer(data=request.data, instance=data, partial=True,context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = quizChoiceModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
# </editor-fold>
