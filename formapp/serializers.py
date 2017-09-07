from rest_framework import serializers
from formapp.models import FormDetail, FormResponse


class FormDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormDetail
        fields = ('id', 'title', 'user', 'description', 'status', 'fields',
                  'need_login', 'created', 'modified')
