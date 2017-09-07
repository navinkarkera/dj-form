from formapp.models import FormDetail
from formapp.serializers import FormDetailSerializer
from rest_framework import generics

# Create your views here.


class FormDetailList(generics.ListCreateAPIView):
    def get_queryset(self):
        user = self.request.user
        return FormDetail.objects.filter(user=user)

    serializer_class = FormDetailSerializer


class FormDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        user = self.request.user
        return FormDetail.objects.filter(user=user)

    serializer_class = FormDetailSerializer
