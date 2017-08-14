from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField, ArrayField

# Create your models here.


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FormDetail(BaseModel):
    STATUS = ((0, 'Inactive'), (1, 'Active'))
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField('Form title', max_length=200)
    description = models.TextField('Brief about your Form')
    status = models.IntegerField(choices=STATUS)
    fields = ArrayField(JSONField())

    def __str__(self):
        return self.title


class FormResponse(BaseModel):
    form = models.ForeignKey(FormDetail, on_delete=models.CASCADE)
    response = JSONField()

    def __str__(self):
        return self.form.title
