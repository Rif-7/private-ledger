from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model


# Create your models here.

class User(AbstractUser):
    pass


class Ledger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ledges")
    cat =  models.CharField(max_length=15)
    description = models.TextField()
    amount = models.IntegerField()
    to = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "user": self.id,
            "cat": self.cat,
            "description": str(self.description),
            "amount": self.amount,
            "to": self.to,
            "date": self.date.strftime("%b %d %Y, %I:%M %p")
        }
    

class Categorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cats")
    name = models.CharField(max_length=15)