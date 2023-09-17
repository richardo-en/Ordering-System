from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

    
class TagColors(models.Model):
    BLUE = "btn-primary"  
    GRAY = "btn-secondary"
    GREEN = "btn-success"
    RED = "btn-danger"
    YELLOW = "btn-warning"
    CYAN = "btn-info"
    WHITE = "btn-light"
    DARK = "btn-dark"

    COLOR_CHOICE = [
        (BLUE, "Blue"),
        (GRAY, "Gray"),
        (GREEN, "Green"),
        (RED, "Red"),
        (YELLOW, "Yellow"),
        (CYAN, "Cyan"),
        (WHITE, "White")
        ]
    
    color_class = models.CharField(max_length=20, choices=COLOR_CHOICE, default=BLUE)

class OrderPlace(models.Model):
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=20, choices=TagColors.COLOR_CHOICE, default=TagColors.BLUE)

    def __str__(self):
        return self.name

class OrderType(models.Model):
    name = models.CharField(max_length=40)
    color = models.CharField(max_length=20, choices=TagColors.COLOR_CHOICE, default=TagColors.BLUE)

    def __str__(self):
        return self.name

class Goods(models.Model):
    name = models.CharField(max_length=40 , null=False)
    place = models.ForeignKey(OrderPlace, blank=True, on_delete= models.SET_NULL, null=True)
    type = models.ForeignKey(OrderType, blank=True, on_delete= models.SET_NULL, null=True)
    price = models.FloatField()
    total_count = models.IntegerField(null=True,  blank=True)
    count = models.IntegerField(validators=[MinValueValidator(1)])
    note = models.CharField(max_length = 200, null=True, blank = True)

    READY = "Ready"
    INPROGRESS = "In progress"
    DELIVERED = "Delivered"
    CANCELED = "Canceled"

    CURRENT_STATUS = [
        (READY, "Done"),
        (INPROGRESS, "In progress"),
        (DELIVERED, "Delivered"),
        (CANCELED, "Canceled")
        ] 

class CustomUser(AbstractUser):
    ADMIN = "Admin"
    EMPLOYEE = "Employee"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (EMPLOYEE, "Employee")] 
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE)
    places = models.ManyToManyField(OrderPlace, blank=True)

    def __str__(self):
        return self.username 
    
class Tables(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(validators=[MinValueValidator(1)])