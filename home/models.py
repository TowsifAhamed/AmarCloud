from django.db import models
from django.conf import settings

class File(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, null=True)
    files = models.FileField(upload_to='files/')
    sizef = models.IntegerField(default=0)

    def __str__(self):
        return self.user