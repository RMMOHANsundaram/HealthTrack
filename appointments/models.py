from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    specialization = models.CharField(
        max_length=100
    )

    available_days = models.CharField(
        max_length=200,
        default='Monday-Friday'
    )

    def __str__(self):
        return f"Dr. {self.user.get_full_name()}"


class TimeSlot(models.Model):

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    time = models.TimeField()

    is_booked = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.doctor} - {self.date} - {self.time}"


class Appointment(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='student_appointments'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    slot = models.ForeignKey(
        TimeSlot,
        on_delete=models.CASCADE
    )

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.username} - {self.doctor}"