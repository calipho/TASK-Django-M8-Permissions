from django.contrib.auth.models import User
from django.db import models
from .permissions import IsTrueAfterCancel


class Flight(models.Model):
    destination = models.CharField(max_length=100)
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    miles = models.PositiveIntegerField()

    def __str__(self):
        return "to %s at %s" % (self.destination, str(self.time))


class Booking(models.Model):
    flight = models.ForeignKey(
        Flight, on_delete=models.CASCADE, related_name="bookings"
    )
    date = models.DateField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    passengers = models.PositiveIntegerField()

    def __str__(self):
        return "%s: %s" % (self.user.username, str(self.flight))
