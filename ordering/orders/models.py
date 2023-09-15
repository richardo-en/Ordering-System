from django.db import models
from accounts.models import Goods
from django.core.validators import RegexValidator

class OverallOrder(models.Model):
    DONE = "Done"
    INPROGRESS = "In progress"
    CANCELED = "Canceled"

    OVERALL_STATUS = [
        (DONE, "Done"),
        (INPROGRESS, "In progress"),
        (CANCELED, "Canceled")
        ]   
    
    PANDA = "PANDA"
    BOLT = "BOLT"
    RAJON = "RAJON"
    ROZVOZ = "ROZVOZ"
    PANDA_CASH = "PANDA_CASH"

    ORDER_TYPE = [
        (PANDA, "PANDA"),
        (PANDA_CASH, "PANDA_CASH"),
        (BOLT, "BOLT"),
        (RAJON, "RAJON"),
        (ROZVOZ, "ROZVOZ"),
    ]
    
    order_type = models.CharField(
        max_length=20,
        choices=ORDER_TYPE,
        default=RAJON,
    )

    name = models.CharField(max_length=50)
    price = models.FloatField()
    goods = models.ManyToManyField(Goods, blank=True)
    phone_regex = RegexValidator(
        regex=r'^\d{9,13}$',
        message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed."
    )

    note = models.CharField(max_length=200, null=True, blank=True)
    mobile_phone = models.CharField(validators=[phone_regex], max_length=13, blank=True)
