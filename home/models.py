from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    job = models.CharField(max_length=255)
    description = models.CharField(max_length=2_555)


class massage(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='senderuser')
    reciever = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='friend')
    text = models.CharField(max_length=2_555, null=True)
    picture = models.ImageField(null=True, blank=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return (str(self.sender))
