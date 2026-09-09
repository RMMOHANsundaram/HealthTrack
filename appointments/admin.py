from django.contrib import admin

from .models import Doctor, TimeSlot, Appointment


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'specialization',
        'available_days'
    )

    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name'
    )


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):

    list_display = (
        'doctor',
        'date',
        'time',
        'is_booked'
    )

    list_filter = (
        'date',
        'is_booked'
    )


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = (
        'student',
        'doctor',
        'slot',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
    )