from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import HealthRecord, Prescription
from .forms import HealthRecordForm, PrescriptionForm

from appointments.models import Appointment, Doctor


@login_required
def my_records(request):

    records = HealthRecord.objects.filter(
        student=request.user
    ).prefetch_related('prescriptions').order_by('-created_at')

    return render(
        request,
        'records/my_records.html',
        {'records': records}
    )


@login_required
def record_detail(request, record_id):

    record = get_object_or_404(
        HealthRecord,
        id=record_id
    )

    # Student can see only their own record
    if record.student != request.user:

        try:
            doctor = request.user.doctor

            if record.doctor != doctor:
                return redirect('dashboard')

        except Doctor.DoesNotExist:
            return redirect('dashboard')

    return render(
        request,
        'records/record_detail.html',
        {'record': record}
    )


@login_required
def create_record(request, appointment_id):

    try:
        doctor = request.user.doctor
    except Doctor.DoesNotExist:
        return redirect('dashboard')

    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        doctor=doctor
    )

    if request.method == 'POST':

        form = HealthRecordForm(request.POST)

        if form.is_valid():

            record = form.save(commit=False)

            record.doctor = doctor
            record.student = appointment.student
            record.appointment = appointment

            record.save()

            return redirect(
                'add_prescription',
                record_id=record.id
            )

    else:

        form = HealthRecordForm(
            initial={
                'student': appointment.student,
                'appointment': appointment
            }
        )

    return render(
        request,
        'records/create_record.html',
        {
            'form': form,
            'appointment': appointment
        }
    )


@login_required
def add_prescription(request, record_id):

    record = get_object_or_404(
        HealthRecord,
        id=record_id
    )

    try:
        doctor = request.user.doctor
    except Doctor.DoesNotExist:
        return redirect('dashboard')

    if record.doctor != doctor:
        return redirect('dashboard')

    if request.method == 'POST':

        form = PrescriptionForm(request.POST)

        if form.is_valid():

            prescription = form.save(commit=False)

            prescription.health_record = record

            prescription.save()

            return redirect(
                'record_detail',
                record_id=record.id
            )

    else:

        form = PrescriptionForm()

    return render(
        request,
        'records/add_prescription.html',
        {
            'form': form,
            'record': record
        }
    )


@login_required
def doctor_records(request):

    try:
        doctor = request.user.doctor
    except Doctor.DoesNotExist:
        return redirect('dashboard')

    records = HealthRecord.objects.filter(
        doctor=doctor
    ).select_related(
        'student'
    ).order_by('-created_at')

    return render(
        request,
        'records/doctor_records.html',
        {
            'records': records
        }
    )