from django.urls import path
from . import views


urlpatterns = [

    path(
        'doctors/',
        views.doctors,
        name='doctors'
    ),

    path(
        'book/<int:doctor_id>/',
        views.book_appointment,
        name='book_appointment'
    ),

    path(
        'my/',
        views.my_appointments,
        name='my_appointments'
    ),

    path(
        'cancel/<int:appointment_id>/',
        views.cancel_appointment,
        name='cancel_appointment'
    ),

    path(
        'doctor/',
        views.doctor_appointments,
        name='doctor_appointments'
    ),

    path(
        'complete/<int:appointment_id>/',
        views.complete_appointment,
        name='complete_appointment'
    ),
]