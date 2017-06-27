from django.db import models
from django.utils import timezone


class Order(models.Model):
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    sended_date = models.DateTimeField(
            blank=True, null=True)

    def send(self):
        self.sended_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
