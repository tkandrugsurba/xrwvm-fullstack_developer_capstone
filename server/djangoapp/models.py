from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Name of the car make
    description = models.TextField()  # Description of the car make

    # String representation of the CarMake model
    def __str__(self):
        return self.name  # Return the car make's name


# Car Model model
class CarModel(models.Model):
    # Many-to-One relationship to CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  
    name = models.CharField(max_length=100)  # Name of the car model

    # Define choices for car types
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
    ]

    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')  # Car type
    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(2015)
        ]
    )  # Year of the car model

    # String representation of the CarModel model
    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"  # Return car make name, model name, and year
