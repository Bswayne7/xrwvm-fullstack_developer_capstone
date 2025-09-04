from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now


# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Any other fields you’d like, e.g., country of origin
    country = models.CharField(max_length=100, default="Unknown")

    def __str__(self):
        return self.name   # Display the car make name


# Car Model model
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One
    dealer_id = models.IntegerField(default=0)  # Refers to dealer in Cloudant DB
    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('COUPE', 'Coupe'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')

    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )

class Dealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip
        
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
