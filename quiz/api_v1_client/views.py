from django.contrib.auth import get_user_model
from rest_framework import generics, status, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from quiz.api_v1_client.serializers import quizClientQuestionSerializer, quizClientQuestionCreateSerializer
from quiz.models import quizQuestionModel

User = get_user_model()


class quizClientQuestionCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = quizClientQuestionSerializer
    queryset = quizQuestionModel.objects.all()
    permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    # pagination_class = LimitOffsetPagination
    search_fields = ["title", ]
    filter_backends = (filters.SearchFilter,)

    def list(self, request, *args, **kwargs):
        # s_name_brand = quizQuestionModel.objects.filter(title__startwith="s")
        serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
                                         context={"request": request})
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = quizClientQuestionCreateSerializer(data=request.data,context={"request": request})
        print(serializer,"==============serilizers")
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class quizClientQuestionDetailsAPIView(APIView):
    serializer_class = quizClientQuestionSerializer
    # permission_classes = (IsAuthenticated,)
    # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    pagination_class = None

    def get(self, request, slug):
        data = quizQuestionModel.objects.get(slug=slug)
        serializer = quizClientQuestionSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, slug):
        data = quizQuestionModel.objects.get(slug=slug)
        serializer = quizClientQuestionSerializer(data=request.data, instance=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        data = quizQuestionModel.objects.get(slug=slug)
        data.delete()
        return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)


#
# class quizClientQuestionCreateGenericsView(generics.ListAPIView, generics.CreateAPIView):
#     serializer_class = quizClientQuestionSerializer
#     queryset = quizQuestionModel.objects.all()
#     permission_classes = (IsAuthenticated,)
#     # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
#     # pagination_class = LimitOffsetPagination
#     search_fields = ["title", ]
#     filter_backends = (filters.SearchFilter,)
#
#     def list(self, request, *args, **kwargs):
#         # s_name_brand = quizQuestionModel.objects.filter(title__startwith="s")
#         serializer = self.get_serializer(self.paginate_queryset(self.filter_queryset(self.get_queryset())), many=True,
#                                          context={"request": request})
#         return self.get_paginated_response(serializer.data)
#
#     def post(self, request):
#         serializer = quizClientQuestionCreateSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class quizClientQuestionDetailsAPIView(APIView):
#     serializer_class = quizClientQuestionSerializer
#     # permission_classes = (IsAuthenticated,)
#     # authenticate_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
#     pagination_class = None
#
#     def get(self, request, slug):
#         data = quizQuestionModel.objects.get(slug=slug)
#         serializer = quizClientQuestionSerializer(data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, slug):
#         data = quizQuestionModel.objects.get(slug=slug)
#         serializer = quizClientQuestionSerializer(data=request.data, instance=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, slug):
#         data = quizQuestionModel.objects.get(slug=slug)
#         data.delete()
#         return Response({"data": "Objects Deleted Successfully"}, status=status.HTTP_202_ACCEPTED)
