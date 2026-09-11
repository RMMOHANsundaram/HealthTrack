from django.contrib import admin

from .models import HealthRecord, Prescription


@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'doctor',
        'diagnosis',
        'created_at'
    )

    list_filter = (
        'created_at',
    )

    search_fields = (
        'student__username',
        'student__first_name',
        'student__last_name',
        'diagnosis'
    )


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):

    list_display = (
        'medicine_name',
        'dosage',
        'duration',
        'health_record'
    )

    search_fields = (
        'medicine_name',
        'health_record__student__username'
    )