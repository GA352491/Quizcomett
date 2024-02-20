from django.db import models
from accounts.models import CustomUser
from questioners.models import Category


# Create your models here.
class Stats(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    marks_obtained = models.IntegerField(blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user
