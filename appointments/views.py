from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Doctor, TimeSlot, Appointment


@login_required
def doctors(request):

    doctors = Doctor.objects.all()

    return render(
        request,
        'accounts/appointments/doctors.html',
        {
            'doctors': doctors
        }
    )


@login_required
def book_appointment(request, doctor_id):

    doctor = get_object_or_404(
        Doctor,
        id=doctor_id
    )

    slots = TimeSlot.objects.filter(
        doctor=doctor,
        is_booked=False
    ).order_by(
        'date',
        'time'
    )

    if request.method == 'POST':

        slot_id = request.POST.get('slot')
        reason = request.POST.get('reason')

        slot = get_object_or_404(
            TimeSlot,
            id=slot_id,
            doctor=doctor,
            is_booked=False
        )

        Appointment.objects.create(
            student=request.user,
            doctor=doctor,
            slot=slot,
            reason=reason
        )

        slot.is_booked = True
        slot.save()

        return redirect('my_appointments')

    return render(
        request,
        'accounts/appointments/book.html',
        {
            'doctor': doctor,
            'slots': slots
        }
    )


@login_required
def my_appointments(request):

    appointments = Appointment.objects.filter(
        student=request.user
    ).order_by('-created_at')

    return render(
        request,
        'accounts/appointments/my_appointments.html',
        {
            'appointments': appointments
        }
    )


@login_required
def cancel_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        student=request.user
    )

    if appointment.status != 'completed':

        appointment.status = 'cancelled'

        appointment.slot.is_booked = False
        appointment.slot.save()

        appointment.save()

    return redirect('my_appointments')


@login_required
def doctor_appointments(request):

    try:
        doctor = request.user.doctor

    except Doctor.DoesNotExist:
        return redirect('dashboard')

    appointments = Appointment.objects.filter(
        doctor=doctor
    ).order_by(
        'slot__date',
        'slot__time'
    )

    return render(
        request,
        'accounts/appointments/doctor_appointment.html',
        {
            'appointments': appointments
        }
    )


@login_required
def complete_appointment(request, appointment_id):

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor__user=request.user
    )

    appointment.status = 'completed'

    appointment.save()

    return redirect('doctor_appointments')