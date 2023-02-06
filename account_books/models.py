from django.db import models
from users.models import User

# Create your models here.
class AccountBook(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(
        User,
        related_name="account_details",
        on_delete=models.CASCADE,
    )
    date = models.DateField()
    amount = models.IntegerField()
    memo = models.CharField(max_length=100)
