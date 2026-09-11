from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from appointments.models import Appointment, Doctor
from records.models import HealthRecord, Prescription


@login_required
def dashboard(request):

    # Only admin can access analytics dashboard
    if not request.user.is_superuser:
        return redirect('dashboard')

    # Basic counts
    total_students = User.objects.filter(
        userprofile__role='student'
    ).count()

    total_doctors = Doctor.objects.count()

    total_appointments = Appointment.objects.count()

    completed_appointments = Appointment.objects.filter(
        status='completed'
    ).count()

    pending_appointments = Appointment.objects.filter(
        status='pending'
    ).count()

    cancelled_appointments = Appointment.objects.filter(
        status='cancelled'
    ).count()

    total_records = HealthRecord.objects.count()

    total_prescriptions = Prescription.objects.count()

    # Appointment statistics by status
    appointment_status = {
        'pending': pending_appointments,
        'completed': completed_appointments,
        'cancelled': cancelled_appointments,
        'confirmed': Appointment.objects.filter(
            status='confirmed'
        ).count(),
    }

    # Recent health records
    recent_records = HealthRecord.objects.select_related(
        'student',
        'doctor'
    ).order_by('-created_at')[:10]

    context = {
        'total_students': total_students,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'completed_appointments': completed_appointments,
        'pending_appointments': pending_appointments,
        'cancelled_appointments': cancelled_appointments,
        'total_records': total_records,
        'total_prescriptions': total_prescriptions,
        'appointment_status': appointment_status,
        'recent_records': recent_records,
    }

    return render(
        request,
        'analytics/dashboard.html',
        context
    )