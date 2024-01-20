from django.db import models

# Create your models here.

class PracticeModel(models.Model):
    Roll = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField()
    Bank_balance = models.BigIntegerField()
    Agree_the_term = models.BooleanField()
    Date_of_birth = models.DateField()
    Max_holding_breath = models.DurationField()
    generic_ip_address_field = models.GenericIPAddressField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    slug_field = models.SlugField()
    time_field = models.TimeField()
    url_field = models.URLField()