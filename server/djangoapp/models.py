from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Car Make Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


# Car Model Model
class CarModel(models.Model):
    # Many-to-one relationship with CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    # Dealer ID from Cloudant database
    dealer_id = models.IntegerField()

    # Model details
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]
    type = models.CharField(max_length=20, choices=CAR_TYPES)

    # Year with limits
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(2023)
        ]
    )

    # Extra field (optional)
    color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.type}, {self.year})"

