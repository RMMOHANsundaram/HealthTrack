from django.db import models
from django.contrib.auth.models import User
from appointments.models import Doctor, Appointment


class HealthRecord(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='health_records'
    )

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='health_records'
    )

    appointment = models.ForeignKey(
        Appointment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    diagnosis = models.TextField()
    symptoms = models.TextField(blank=True)
    treatment = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username} - {self.diagnosis}"


class Prescription(models.Model):
    health_record = models.ForeignKey(
        HealthRecord,
        on_delete=models.CASCADE,
        related_name='prescriptions'
    )

    medicine_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    instructions = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.medicine_name