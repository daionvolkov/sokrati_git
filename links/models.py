from django.db import models
from django.contrib.auth.models import User


class Links(models.Model):
    oldLink = models.URLField(max_length=250)
    newLink = models.CharField(max_length=250, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save()

    def __str__(self):
        return self.newLink

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
