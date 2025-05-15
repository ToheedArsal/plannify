from django.db import models
from django.forms.models import model_to_dict


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        abstract = True

