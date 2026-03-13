from django.db import models

# Create your models here.

class Subscription(models.Model):

    email = models.EmailField()

    subscription_id = models.CharField(max_length=200)

    plan = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
