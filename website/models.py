from django.db import models
from django.core.exceptions import ValidationError

def validate_three_digits(value):
    if not (100 <= value <= 999):
        raise ValidationError('The value must be a three-digit number.')

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email  = models.CharField(max_length=100)
    phone  = models.CharField(max_length=50)
    address  = models.CharField(max_length=200)
    city  = models.CharField(max_length=50)
    state  = models.CharField(max_length=50)
    zipcode  = models.CharField(max_length=50)
    age = models.PositiveIntegerField(validators=[validate_three_digits])

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

